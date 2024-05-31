# Mouse Jiggler 

### Usage

Welcome to mouse-jiggler! This simple program will keep your mouse jiggling whenever you want and can be customized to your liking for whatever your use case may be. Once set up, it will work in the background exactly like any other program running on your machine and work through keyboard shortcuts, exactly like copy and paste. To start the jiggler, all you have to do is press `cmd+shift+u` and to stop it simply press `cmd+shift+k`. That's it, it's really that simple! There will also be notifications communicating the status, like when you enable it you'll get a standard Mac notification (like all the others) informing you that it is enabled and the same for when you turn it off. 

Heard enough and wanna get started? Read the [easiest setup method](https://github.com/UmairK5669/mouse-jiggler/blob/main/README.md#easiest-setup-method) section to get this up and running in as little as a minute!

> [!NOTE]
> This project currently only supports MacOS however, support for other operating systems is coming soon!

### Easiest Setup Method 

This project is available to download through Python's package manager; `pip`

We will be running this in a `tmux` session to ensure the program can run in the background without issues

1. Ensuring Python and `tmux` are installed

Install the `brew` package manager [here](https://brew.sh/)

Once installed, run `brew install Python` to install Python, then `brew install tmux` to install tmux 

> [!TIP]
> If this causes any errors in regards to not being able to find brew, refer to the homebrew official documentation [here](https://docs.brew.sh/Installation)

2. Start a `tmux` session with: `tmux new-session -s mysession`

      Replace `mysession` with your desired session name

3. Run `pip3 install mouse-jiggler-macos` to install the mouse-jiggler package

4. Once installed, simply run `jiggler` and you are good-to-go!

> [!TIP]
> Verify installation correctly by pressing `cmd+shift+u` to start the jiggler, you should see a notification in the top-right corner (Remember `cmd+shift+k` to turn off)

Close the terminal, if it says "terminate session" that is okay! Terminating the `tmux` session won't close the program

> [!CAUTION]
> If your computer sleeps, the program will still be running however, if the computer shuts down the program will unfortunately end. You will have restore the `tmux` session manually which can be done by doing steps 2 and 4 again. 

### Not-so-simple setup method

1. Clone the Repo: `git clone https://github.com/UmairK5669/mouse-jiggler.git`

2. Install the dependencies: `pip3 install -r requirements.txt`
3. Enter the directory where the mouse jiggler code is present: `cd mouse_jiggler`

4. Run the program: `python3 jiggler.py`

### Using Tmux

#### Steps for using Tmux in Terminal

1. Install `tmux` using Homebrew: `brew install tmux`

2. Start a `tmux` session: `tmux new-session -s mysession`

      Replace `mysession` with your desired session name

 3. Start the process in the `tmux` session: `python3 'path/to/jiggler.py'`

> [!CAUTION]
> You might want to install the dependencies again in the `tmux` session as it could cause issues if you don't

4. Close the Terminal, and terminate this process.

 Your jiggler is setup in the background and won't end process when your computer sleeps. In the event of a computer restart, you will need to restore the `tmux` session manually.

 ### Author Thank You 

 Thank you for getting this far with my app, I really hope you were able to set it up and use it without issues. Please don't hesitate to contact me for any issues or for collaboration as I'm always up for innovation! Reach out via email or social links from my [GitHub](https://github.com/UmairK5669) profile. Thanks 😄!
   
