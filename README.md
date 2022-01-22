# gorp


### Installation (macos):

arm64:

```shell
curl -s https://api.github.com/repos/jayshrivastava/gorp/releases/latest \
| grep "browser_download_url" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -

sudo chmod +x gorp
sudo cp gorp /usr/local/bin
rm gorp 
rm gorp_intel

```

x86:

```shell
curl -s https://api.github.com/repos/jayshrivastava/gorp/releases/latest \
| grep "browser_download_url" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -

rm gorp 
mv gorp_intel gorp

sudo chmod +x gorp
sudo cp gorp /usr/local/bin
rm gorp 

```

### Uninstall
```shell
sudo rm /usr/local/bin/gorp
```



