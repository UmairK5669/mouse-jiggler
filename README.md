# Mouse Jiggler 

> [!NOTE]
> This currently only works for MacOS however, support for other operating systems coming soon!

### Steps to Setup

1. Clone the Repo: `git clone https://github.com/UmairK5669/mouse-jiggler.git`

2. Install the dependencies: `pip install -r requirements.txt`

3. Simply run the program: `python3 jiggler.py`

Your program should be ready to go, simply use the shortcuts 'cmd' + 'shift' + 'u' to start jiggling and 'cmd' + 'shift' + 'k' to stop jiggling. 

### Using Tmux

It's recommended to have this running in a `tmux` session so it can run in the background without issues. 

#### Steps for using Tmux in Terminal

1. Install `tmux` using Homebrew: `brew install tmux`

> [!TIP]
> If you don't have the `brew` package manager installed, please install it [here](https://brew.sh/)

2. Start a `tmux` session: `tmux new-session -s mysession`

      Replace `mysession` with your desired session name

 3. Start the process in the `tmux` session: `python3 'path/to/jiggler.py'`

> [!CAUTION]
> You might want to install the dependencies again in the `tmux` session as it could cause issues if you don't

4. Close the Terminal, and terminate this process.

 Your jiggler is setup in the background and won't end process when your computer sleeps. In the event of a computer restart, you will need to restore the `tmux` session manually.

 ### Author Thank You 

 Thank you for getting this far with my app, I really hope you were able to set it up and use it without issues. Please don't hesitate to contact me for any issues or for collaboration as I'm always up for innovation! Reach out via email or social links from my [GitHub](https://github.com/UmairK5669) profile. Thanks 😄!
   
