# localstack_template


Localstack ile çalışan AWS servislerini yerelde kullanmak için gerekli olan docker-compose dosyası ve kullanım örnekleri.

## Kullanım

Repo'yu klonlayın.

```bash
git clone https://github.com/Mertozturkk/localstack_template.git
```

Öncelikle terminalden kendi makinenizde bir aws profili oluşturmanız gerekiyor. Bu işlemi yapmak için aşağıdaki komutu çalıştırın.
Eğer aws cli kurulu değilse [dokumantasyonu](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) takip edin.


```bash
aws configure --profile localstack_dev
```
key değeleri aşağıdaki gibi olmalıdır.

```bash
AWS Access Key ID [None]: test 
AWS Secret Access Key [None]: test
Default region name [None]: eu-central-1
Default output format [None]: 
```

Localstack çalıştırmak için aşağıdaki komutu çalıştırın.

```bash
docker-compose up -d
```

İsterseniz -d parametresini kaldırarak logları görebilirsiniz.

```bash
alias awsls="aws --endpoint-url=http://localhost:4566"
```

Yukarıdaki komutu kullanarak aws cli komutlarınızı localstack üzerinde çalıştırabilirsiniz python dosyalarında örnek komutlar mvcut


