# react-styled-components-cli 💅
A CLI that generates components using the [Styled Components](https://styled-components.com) syntax.

The *rcs* CLI automates the creation of React Functional Components using the following pattern:  
<pre><code>.
|- components/  
|  |- Home/
|  |  |- index.tsx  
|  |  |- Home.tsx  
|  |  |- Home.styles.tsx
</code></pre>

### ⚠️⚠️⚠️ THIS IS NOT A CLI FOR ALL USE CASES ⚠️⚠️⚠️
The main objective is provide a CLI for those who want a easy way to create React.FC inside isolated directories. If you don`t want to follow this pattern, this is not a good choice.  

### YES! THIS IS A VERY **VERY** SPECIFIC CLI 🤷‍♂
Probably this pattern do not fit for anyone else. Who cares? 😅 Feel free to fork this and customize to suit your own needs.

# Instalation
### Prerequisites
- You will need to install [Python 3 🐍](https://www.python.org/downloads/). The good news: Linux brings this by default! Try running `python3` in your terminal. If it prints something like this:
> Python 3.7.3 (default, Apr  3 2019, 05:39:12)   
[GCC 8.3.0] on linux  
Type "help", "copyright", "credits" or "license" for more information.  
\>>>  
  
... so Python 3 is installed. You can just follow the other steps.  
<small style="float: right;">Hit `Ctrl + D` to close the python CLI. You wellcome.</small>  

### Alright, the steps:
1. Clone or download this repo.
2. Enter the folder.
3. Run `source ./setup.sh` to add the `rcs` command as a _system alias_. So, now, you can run it anywhere.
> **Note**: if you do not use **bash** or **zsh** the setup script will not run as expected. In this case, try to add the alias manually in your ._somethingrc_ file.

> **Optionally** you can just run `python3 rcs c MyComponent` in your cloned directory and copy/paste the files to another location. You decide.
  
4. Finally, to use this CLI, you will need to create a file named as `rcs.conf.json` in the root path of your React projects. This file will contains the default flags for the CLI. It will not work as expected if you did not create the file.
> **File content**: {"is_native": false, "is_jsx": true}  
<small>I hope you are familiar with the JSON syntax. Good luck.</small>

5. THERE ARE NO 5. THATS ALL!!! 🎆😄 Type `rcs help` and reed the docs.

[MIT](https://opensource.org/licenses/MIT) © [Erick Vieira](erickvieira.dev) | 2020