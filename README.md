### Run Ollama with docker image
```sh
docker run -d --name ollama --restart always \
    -v $HOME/.ollama:/root/.ollama \
    -p 11434:11434 \
    ollama/ollama:0.11.8

docker exec -it ollama ollama --help
docker exec -it ollama ollama pull gemma3
docker exec -it ollama ollama pull gemma3:27b
docker exec -it ollama ollama pull llama3.2
docker exec -it ollama ollama pull llama3.3
docker exec -it ollama ollama pull mistral
docker exec -it ollama ollama pull gpt-oss:20b
```

### VM setup steps
```sh
# Create VM with Ubuntu Desktop image
# install oh-my-zsh
sudo apt-get update
sudo apt update
sudo apt-get install zsh curl git
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# update default theme in ~/.zshrc
sudo apt-get install fonts-powerline 

# download VS Code package and install
sudo dpkg -i code_1.101.2-1750797935_amd64.deb

# rename hostname after cloned from the root image
sudo hostnamectl hostname llm-developement
# change hostname in /etc/hosts

# install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo usermod -aG docker $USER

# install python
sudo apt-get update
sudo apt-get install python3 python3-dev python3-pip python3-venv

# install venv module
python3 -m venv .venv

# update global git config
git config --global --add "user.name" "Hung Yip"
git config --global --add "user.email" "kwonghung.yip@gmail.com"
```

### References