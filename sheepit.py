{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JeNg1Yj8c-Xx"
      },
      "source": [
        "Get Dependencies"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "q2aL4cibbWui",
        "vscode": {
          "languageId": "python"
        }
      },
      "outputs": [],
      "source": [
        "#Info about the runtime\n",
        "!cat /etc/os-release\n",
        "!nvidia-smi\n",
        "!nvcc --version\n",
        "\n",
        "#This first Block is required as some weird behaviors with libtcmalloc appeared in the colab VM. \n",
        "import os\n",
        "os.environ[\"LD_PRELOAD\"] = \"\"\n",
        "!apt update\n",
        "!apt remove libtcmalloc-minimal4\n",
        "!apt install libtcmalloc-minimal4\n",
        "os.environ[\"LD_PRELOAD\"] = \"/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4\" #no idea if libtcmalloc_minimal.so.4 or libtcmalloc_minimal.so.4.5.3 works better\n",
        "!echo $LD_PRELOAD\n",
        "\n",
        "#This is for Blender, GPU and sheepit.\n",
        "!apt update\n",
        "!apt install libboost-all-dev\n",
        "!apt install libgl1-mesa-dev\n",
        "!apt install libglu1-mesa \n",
        "!apt install libsm-dev\n",
        "!apt install libxkbcommon0"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oC3OE5XqyJPr"
      },
      "source": [
        "Enter you username and public key (can be found under profile>keys)\n",
        "You have to run this block as well"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HvfliuWddB2H",
        "vscode": {
          "languageId": "python"
        }
      },
      "outputs": [],
      "source": [
        "#@title Setup\n",
        "#@markdown Enter some dogshit \n",
        "username = \"\" #@param {type: \"string\"}\n",
        "key = \"\" #@param {type: \"string\"}\n",
        "computemethod = \"GPU\" #@param [\"GPU\", \"CPU\"] {allow-input: false}\n",
        "downloadUrl = \"https://www.sheepit-renderfarm.com/media/applet/client-latest.php\"\n",
        "#@markdown ---\n",
        "!wget $downloadUrl -O client.jar\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3rYxBLeaeSA2"
      },
      "source": [
        "# **Run this to start**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KbE3Ex53eX0J",
        "vscode": {
          "languageId": "python"
        }
      },
      "outputs": [],
      "source": [
        "if computemethod == \"CPU\":\n",
        "    !java -jar client.jar -ui oneLine/text -cache-dir /content/cache -compute-method $computemethod -login $username -password $key -ui text\n",
        "else:\n",
        "    !java -jar client.jar -ui oneLine/text -cache-dir /content/cache -compute-method GPU -gpu OPTIX_0 -login $username -password $key -ui text"
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "name": "sheepit on web.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
