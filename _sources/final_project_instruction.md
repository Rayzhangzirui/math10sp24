# Final Project Instruction

## Goal

The purpose of the final project is to submit a notebook project which analyzes a dataset of your choice. This type of project could look great in a portfolio when applying to internships and jobs.



## Logistics
The following are requirements to receive a passing score on the final project.
* Due date: 11:59pm, Wednesday of the Finals Week.
* Submission: submit .ipynb and pdf file to gradescope.
* This is an individual project.
* The primary focus of the project must be on something involving data, and primarily using one or more datasets that weren't covered in Math 10.  You can use datasets that are built in to a Python library like Seaborn or scikit-learn, or you can upload the dataset to Deepnote yourself, such as a dataset that you downloaded from Kaggle, that you got from [openml.org](https://www.openml.org/), or that you got from UC Irvine's own [Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).  
* The project should clearly build on the Math 10 material.  If you're an expert in Python material that was not covered in Math 10, you are of course welcome to use that, but the project should use the topics of Math 10 in an essential way (see the rubric below).
* Answer the questions at the top of the template, especially the question regarding whether you want your project posted in the course notes.  
* Here are examples of student projects: [from Spring 2023](https://christopherdavisuci.github.io/UCI-Math-10-S23/Proj/StudentProjects.html), [from Spring 2022](https://christopherdavisuci.github.io/UCI-Math-10-S22/Proj/StudentProjects.html), [from Winter 2022](https://christopherdavisuci.github.io/UCI-Math-10-W22/Proj/StudentProjects.html), [from Fall 2022](https://christopherdavisuci.github.io/UCI-Math-10-F22/Proj/StudentProjects.html).
* Anything that is taken from another source (either the idea for the project or a piece of code, even if you edit that code) should be explicitly referenced with a link.  (For example, you could write, "The configuration of this Altair chart was adapted from ...").


## Rubric
The course project is worth 20% of the course grade, and we will grade the project out of 40 total points.
* (**Clarity**, 5 points) Is the project clear and well-organized?  Does it use good coding style?  Is the code *Pythonic* (for example, avoiding unnecessary for loops) and *DRY* (avoiding unnecessary repetition)?  Does it explore one or more clearly described datasets, and is it clear where those datasets came from?  Use text and markdown throughout the project to help the reader understand what is going on.  Is the reasoning clear? (It's fine if you have negative results like, "so there is no clear connection between these variables".  In fact, I prefer those sorts of results as opposed to unbelievable claims.)  Give your project a relevant title (like "Species of penguins" rather than "Math 10 project").
* (**EDA**, 5 points) Does the project make essential use of pandas to explore the data?  Using pandas to read and store the data is not sufficient.  It should also be used either to clean the data, or to analyze the data, or for performing *feature engineering*.  Does the project include a variety of interesting charts?  Do we learn something about the data from these charts? 
* (**Machine Learning**, 5 points) Does the project explore the data using a variety of tools from scikit-learn?   Does the project refer to essential aspects of data analysis, such as over-fitting, or the importance of a test set, or dimension reduction, or the difference between classification and regression?
* (**Extra**, 5 points) Does the project include material that was not covered in Math 10?  (This could include different libraries, different machine learning algorithms, or deeper use of the libraries we covered in Math 10.  Some possible topics are included in the *Possible Extra Topics* notebook, but you're very encouraged to choose your own.)

## Advice
Here is some general advice about the project.
* Don't repeat the same technique multiple times unless it's really essential.  For example, having one interesting chart and a different less interesting chart is better than having the same interesting chart made for two different datasets.  (Of course, if you can find a *DRY* way to make many related charts, then that's great.)
* Don't spend too much time searching for the perfect dataset or the perfect idea.  Having a great dataset is less important for the project than exploring the dataset in an interesting way.
* Keep your statements reasonable.  It's beter to say "Therefore, we didn’t see any relationship bewteen A and B."  than try to force a claim that just doesn’t seem true.
* The main point of this project is to show what you've learned in Math 10.  If you were already an expert on Python before the class and you write a project based on different material, that probably won't get a good grade, even if it's very advanced.
* Include many markdown cells (possibly very short, just one sentence) explaining what you are doing.  (These are different from Python comments.)  If you want to use bold text in your markdown cell, surround the text by two stars `**like this**`.  Be sure you're doing this in a markdown cell, as opposed to in a Python comment after a `#` symbol.
* Please err on the side of referencing everything.  If your project is based on an idea you saw somewhere else, that's totally fine, but include a clear link in your project to the original source.  If your project is based on a tutorial, then it will be primarily graded based on what you've added to the tutorial.  For example, do you make it clear that you understand what's happening in the tutorial?


## Frequently asked questions
Q: Is there a length requirement?
* There is no specific length requirement, but as a rough estimate, spending approximately 12 productive hours on the project would be a good amount.  (The word "productive" is important.  Time spent browsing tutorials or datasets is not productive in this sense if you don't end up using that material.)

Q: What should I focus on?
* The primary content should be from one or more of the Math 10 tools (pandas, Altair, scikit-learn).  If you like pandas much more than Altair, for example, then it's okay to go more in-depth in the use of pandas, and less in-depth in the use of Altair, but you still need to include both.

Q: Do I need to get original research results?
* No!  If you explore the data in an interesting way, but can't find any interesting conclusions, that's fine. 
Making logical conclusions based on the data is important, even if those conclusions are ``negative``.
Do not make claims that the data does not support.

Q: What if a lot of my work was done cleaning the data, but it does not appear in the project?
* Include those cleaning steps in the project! (If the work was done outside of Python, like in Excel, then that portion will not count.)

Q: Can I use a different plotting library?
* Yes. What the figure shows is more important than the library used to create it.

Q: What if I'm worried my project is too short?
* It's fine to switch to a different topic halfway through your project.  If you finish what you originally planned and want to start something different, that's fine, even if it uses a different dataset.  This isn't like a history paper where you should have a coherent focus from start to end.

Q: Can you look at my project early?
* I'm happy to give a quick first impression and let you know if I have any immediate suggestions.  (I won't have time to read it thoroughly until the final submission.)

Q: Do I need to post my project in the course notes?
* No, that is totally optional, but it might be a nice idea if you would like to show the project if applying for an internship or grad school, for example.

Q: How can I use an Excel file instead of a CSV file?
* If you have an Excel file (with an extension .xlsx or .xls) instead of a csv file, you can try using `pd.read_excel` instead of `pd.read_csv`. It might be easier to just open the file in Excel, save it as a comma-separated csv file there, and then upload that csv file.  Of course another option is just to open the Excel file in Excel or Google Sheets and then save it as a csv file from there.