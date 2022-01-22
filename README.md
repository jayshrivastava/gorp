# gorp


### Installation (macos):

```shell
curl -s https://api.github.com/repos/jayshrivastava/gorp/releases/latest \
| grep "browser_download_url" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -

sudo chmod +x gorp
sudo cp gorp /usr/local/bin
rm gorp 

```
