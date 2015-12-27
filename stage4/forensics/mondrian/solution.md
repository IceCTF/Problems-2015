You're given a website which contains a video containing some words and abstract art. There's a comment on the website with a hint which we'll need later on "OpenPuff - 1/2 (50%) Maximum". 

On each frame of the video there's a word, if we  write that down and take the first letter of each of them we get the word "webdriver". 

If we take each frame from the video (just the abstract art) and bring it into some photo editor and overlay all the frames (removing the white background). We will see a word saying "torso".

Now if we download the software mention in the hint (OpenPuff) we can see that it's a steganography tool for Windows (Sorry linux users, use wine :P ) and if we put the correct options (1/2 (50%) Maximum) and enter the password "webdriver torso" we will get a strange image that looks like abstract art... again.

If we look back on the videa we can see that it's like 20 mins long, and if we look at the last frame it says "Piet".
Piet is an esoteric programming language that uses the colors of pixels as code. Now we just need a piet interpreter such as npiet. If we feed the image to npiet (Might need to convert the image to a different format) we get the flag
flag: `flag_abstract_art_is_magnificent`
