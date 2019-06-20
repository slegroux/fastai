import spacy
from torchtext.data import Field, TabularDataset
from pathlib import Path
from IPython import embed

# (c) 2019 <sylvainlg@voicea.ai>
sentence = "toto is here"
tokenizer = lambda x: x.split()
print(tokenizer(sentence))
TEXT = Field(sequential=True, tokenize=tokenizer,lower=True)
LABEL = Field(sequential=False, use_vocab=False)

data_folder = Path("data")
text_file = data_folder / "vca_train.txt"


train, val, test = TabularDataset.splits(
    path=text_file,
    train='data/vca_train.txt',
    validation='data/validation.txt',
    test='data/test.txt',
    format='csv',
    fields=[('Text', TEXT), ('Label', LABEL)]
)