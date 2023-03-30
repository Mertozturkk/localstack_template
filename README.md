# localstack_template


Localde çalışan AWS servislerini kullanmak için gerekli olan docker-compose dosyası ve kullanım örnekleri.

## Kullanım

Öncelikle terminalden kendi makinenizde bir aws profili oluşturmanız gerekiyor. Bu işlemi yapmak için aşağıdaki komutu çalıştırın.

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
eğer aws cli kurulu değilse [dokumantasyonu](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) takip edin.

Localstack çalıştırmak için aşağıdaki komutu çalıştırın.

```bash
docker-compose up -d
```

İsterseniz -d parametresini kaldırarak logları görebilirsiniz.

```bash
alias awsls="aws --endpoint-url=http://localhost:4566"
```

Yukarıdaki komutu kullanarak aws cli komutlarınızı localstack üzerinde çalıştırabilirsiniz python dosyalarında örnek komutlar mvcut


