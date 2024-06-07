# Final Project Instruction

## Goal

The purpose of the final project is to submit a notebook project which analyzes a dataset of your choice. This type of project could look great in a portfolio when applying to internships and jobs.



## Logistics
The following are requirements to receive a passing score on the final project.
* Due date: 11:59pm, Wednesday of the Finals Week.
* Submission: submit .ipynb and .pdf file to Canvas>Assignments>Final Project.
* This is an individual project.
* The primary focus of the project must be on something involving data, and primarily using one or more datasets that weren't covered in Math 10.  You can use datasets that are built in to a Python library like Seaborn or scikit-learn, or you can use dataset from [Kaggle](https://https://kaggle.com/), [openml.org](https://www.openml.org/), [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php), etc.
* The project should clearly build on the Math 10 material. If you're an expert in Python material that was not covered in Math 10, you are welcome to use that, but the project should use the topics of Math 10 in an essential way (see the rubric below).
* Answer the questions at the top of the [template](final_project_template.ipynb), especially the question regarding whether you want your project posted in the course notes. If the is "yes", you can also email me to update the notebook or take it down.
* Here are examples of student projects: [from Spring 2023](https://christopherdavisuci.github.io/UCI-Math-10-S23/Proj/StudentProjects.html), [from Spring 2022](https://christopherdavisuci.github.io/UCI-Math-10-S22/Proj/StudentProjects.html), [from Winter 2022](https://christopherdavisuci.github.io/UCI-Math-10-W22/Proj/StudentProjects.html), [from Fall 2022](https://christopherdavisuci.github.io/UCI-Math-10-F22/Proj/StudentProjects.html).
* Anything that is taken from another source (either the idea for the project or a piece of code, even if you edit that code) should be explicitly referenced with a link.  (For example, you could write, "The configuration of this Altair chart was adapted from ...").


## Rubric
The course project is worth 20% of the course grade, and we will grade the project out of 20 total points.
* (**Clarity**, 5 points) Is the project clear and well-organized?  Does it use good coding style?  Is the code *Pythonic* (for example, avoiding unnecessary for loops) and *DRY* (avoiding unnecessary repetition)?  Does it explore one or more clearly described datasets, and is it clear where those datasets came from?  Use text and markdown throughout the project to help the reader understand what is going on.  Is the reasoning sound? (It's fine if you conclude, "so there is no clear connection between these variables"). Give your project a relevant title (like "Species of penguins" rather than "Math 10 project").
* (**EDA**, 5 points) Does the project make essential use of pandas to explore the data?  It should also be used either to clean the data, or to analyze the data, or for performing *feature engineering*.  Does the project include a variety of interesting charts?  Do we learn something about the data from these charts? 
* (**Analysis**, 5 points) Does the project explore the data using a variety of tools from scikit-learn? Does the project refer to essential aspects of data analysis, such as over-fitting, or the importance of a test set, or dimension reduction, or the difference between classification and regression?
* (**Extra**, 5 points) Does the project include material that was not covered in Math 10?  This could include different libraries, different algorithms, or deeper use of the libraries we covered in Math 10.

## Project Advice

Here is some general advice:

- **Avoid Repetition:** Don’t repeat the same technique multiple times unless essential. A variety of different charts is better than the same chart for different datasets.
- **Don't Oversearch:** Don’t spend too much time searching for the perfect dataset or idea. Exploring a dataset in an interesting way is more important than having a perfect dataset.
- **Be Reasonable:** Keep your statements reasonable. It’s better to say, "Therefore, we didn’t see any relationship between A and B," than to force a claim.
- **Show Your Learning:** The main point is to demonstrate what you’ve learned in Math 10. A project based on material outside of what was covered in class won’t score well, even if it's advanced.
- **Use Markdown:** Include many markdown cells to explain what you are doing. These can be very short, even just one sentence. Use `**bold text**` in markdown cells for emphasis, not in Python comments.
- **Reference Everything:** Reference all sources clearly. If your project is based on an idea or tutorial, include a clear link to the original source. Your project will be graded on how well you explain and build on the tutorial content.


## Frequently Asked Questions

**Q: Is there a length requirement?**
- No specific length, but aim to spend about 12 productive hours on the project. Productive means time spent actively working on the project, not just browsing tutorials or datasets.

**Q: What should I focus on?**
- Use tools from Math 10, such as pandas, visualization libraries, and scikit-learn.

**Q: What if much of my work involved data cleaning, but it's not in the project?**
- Include all data cleaning steps in the project. Work done outside Python, like in Excel, won't count.

**Q: Can I use a different plotting library?**
- Yes, the content of the figure is more important than the library used.

**Q: What if I'm worried my project is too short?**
- It's fine to switch topics halfway through. If you finish your original plan and want to start something new with a different dataset, go ahead.

**Q: Do I need to post my project in the course notes?**
- Posting is optional. It can be useful for applications to internships or grad school. You can email me to update or remove it later.

**Q: How can I use an Excel file instead of a CSV file?**
- Use `pd.read_excel` for Excel files. Alternatively, open the Excel file in Excel or Google Sheets, save it as a CSV, and then upload that CSV file.