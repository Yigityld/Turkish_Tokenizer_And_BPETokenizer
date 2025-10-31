from datasets import load_dataset

dataset = load_dataset("musabg/wikipedia-tr-summarization")

train_data = dataset["train"]["text"][0:2000]
from tokenizers import (
    decoders,
    models,
    normalizers,
    pre_tokenizers,
    processors,
    trainers,
    Tokenizer,
)

tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
tokenizer.normalizer = normalizers.Sequence(
    [normalizers.NFD(), normalizers.Lowercase(), normalizers.StripAccents()]
)
print(tokenizer.normalizer.normalize_str("Her merhaba, KONu iyi ilerliyor mu?"))
tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
print(tokenizer.pre_tokenizer.pre_tokenize_str( "ön belirteçleyiciyi test edelim." ))

special_tokens = ["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"]
trainer = trainers.WordPieceTrainer(vocab_size=40000, special_tokens=special_tokens)

tokenizer.train_from_iterator(train_data, trainer=trainer)


encoding = tokenizer.encode("bu tokenizasyon modelini test edelim")
print(encoding.tokens)

cls_token_id = tokenizer.token_to_id("[CLS]")
sep_token_id = tokenizer.token_to_id("[SEP]")

tokenizer.post_processor = processors.TemplateProcessing(
    single=f"[CLS]:0 $A:0 [SEP]:0",
    pair=f"[CLS]:0 $A:0 [SEP]:0 $B:1 [SEP]:1",
    special_tokens=[("[CLS]", cls_token_id), ("[SEP]", sep_token_id)],
)

encoding = tokenizer.encode("bu tokenizasyon modelini test edelim")
print(encoding.tokens)
encoding = tokenizer.encode("bu tokenizasyon modelini test edelim.","Bu ikinci cümle.")
print(encoding.tokens)
print(encoding.type_ids)

tokenizer.decoder = decoders.WordPiece(prefix="##")
print(tokenizer.decode(encoding.ids))
tokenizer.save("tokenizer.json")
