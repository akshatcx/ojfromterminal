sudo pip3 install selenium bs4 halo;

sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4;
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip;
unzip chromedriver_linux64.zip;
rm chromedriver_linux64.zip;
sudo mv chromedriver /usr/bin/chromedriver;
sudo chown root:root /usr/bin/chromedriver;
sudo chmod +x /usr/bin/chromedriver;

#adding geckodriver to your system for running it in firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz;
tar xvfz geckodriver-v0.24.0-linux64.tar.gz;
mv geckodriver ~/.local/bin;
rm -rf geckodriver-v0.24.0-linux64.tar.gz;
#Thats it, jai mata di


