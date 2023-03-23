
# This script is used to configure the environment for the project.
# find shell
SHELL_PATH=$(echo $SHELL
if [ $SHELL_PATH = "/bin/bash" ]; then
echo  export LOCALSTACK_ENDPOINT_URL="http://localhost:4566" >> $HOME/.bash_profile
echo  export AWS_PROFILE="localstack_dev_profile" >> $HOME/.bash_profile
echo  export AWS_DEFAULT_REGION="us-east-1" >> $HOME/.bash_profile
fi

# if SHELL_PATH is /bin/zsh
if [ $SHELL_PATH = "/bin/zsh" ]; then
    echo export 'LOCALSTACK_ENDPOINT_URL="http://localhost:4566"' >> $HOME/.zshrc
    echo export 'AWS_PROFILE="localstack_dev_profile"' >> $HOME/.zshrc
    echo export 'AWS_DEFAULT_REGION="us-east-1"' >> $HOME/.zshrc
fi

echo "Configuring AWS CLI"
aws configure --profile localstack_dev_profile --region us-east-1 --endpoint-url http://localhost:4566
sleep 2
echo "AWS CLI configured successfully"

echo "Alias for localstack endpoint url"
alias awsls="aws --endpoint-url=$LOCALSTACK_ENDPOINT_URL"
sleep 2

