# exchangeCLI

this project offers a CLI for converting currencies


## Usage
Get an API key from [here](https://openexchangerates.org/account/app-ids) and put it inside a config.py file.
Then call the rates.py script via the CLI and provide your base and the target currency

For example, for finding the exchange rate between USD and ZWL you can do the following:

```
python src/rates.py --base USD --target ZWL
```