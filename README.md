[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3746748&assignment_repo_type=AssignmentRepo)

Project Overview
The Digital Repository project, was a proof-of-concept program built upon the notion of David Eagleman's "third death", the death that comes from being forgotten.
A notion that later brought me to realize that few outside the realms of politicians, kings, or celebrities, are ever given a chance to tell their story within the pages of history.
As such the ultimate goal of my Repository program was to delay this supposed third death for as long as possible; allowing the average individual the same privileges as rulers of old, to be remembered.

The program was to function as follows:
An individual will be greeted by the Repository and be given the option to browse the archives for random quotes, to relate to others via an algorithm that searches the archives based on personal similarities, or to simply record a snapshot of their own life.

Terms herby defined as: Listen, Relate, Record,

However, as of time of writing, the Repository can only perform the tasks of Recording and Listening to the degrees of which were originally intended.

Project Narrative

The program was created over the course of three weeks and took an unspecified amount of hours in between day to day work. The process of which should be noted to have been dependent upon the lectures and readings provided in class, as well as various intro-to-python Youtube tutorials.

Reaching Milestone 1 in this project was essentially me writing out the framework for the program and testing out my knowledge in python by writing multiple mini-programs that each fulfilled an aspect of the main Repository.

By Milestone 2 however, I had begun attempting to link the programs before realizing I needed a proper GUI if I was to achieve what I had originally had hoped to do with the Repository, it being an online web-capsule after all. This resulted in most of Milestone 2 being my discovery and learning process with pythons built in GUI system Tkinter.

By the final submission deadline I had successfully linked the original set of programs, including the read/write, the initial entry boxes, and the intricate and time consuming GUI page-to-page button system. However, I was unable to write, or to even begin to fully conceptualize how exactly I was to create a functioning algorithm to parse and display certain files based on similarities in user inputted phrases.

In all though it was an interesting journey, one filled with mishaps, system glitches, and some errors I still don’t quite fully understand. Despite this however, I feel I want to continue to program and to develop this idea, and hopefully branch on and create my own GUI system without the assistance of built in and limited packages like tkinter.

Corrections

In terms of corrections, your comments seemed generally loose towards the program I was creating, giving me the reigns of the project in a sense. To your first comment though I did shoot you an email as I was confused as to the issue, of which you later addressed within your second comment as being an incompatibility between python 2 and python 3.

As for bugs I discovered and work arounds created, there where many

Line 51 I for the button I learned that "command" when running a function will automatically activate that function, rather than activate on press, with the work around being you must use Lambda to allow the functioned to called properly

Line 115 and Line 165 for example define the custom path I was using, but what I found contrary to most tutorials on creating custom directories is that on some versions of python, the directory must be defined as a "raw" strings and thus have an 'r' placed in front of it.
