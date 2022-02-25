# DAX story
When I first started working as a Data Analyst back in 2020, I had lots of fun with Power Bi. Luckily, I had two lovely colleagues who patiently taught me lots of Power Bi tricks. I was introduced to [The Definitive Guide to DAX book](https://www.amazon.com.au/DEFINITIVE-GUIDE-DAX-INTELLIGENCE-MICROSOFT/dp/9353945488/ref=asc_df_9353945488/?tag=googleshopdsk-22&linkCode=df0&hvadid=464180633192&hvpos=&hvnetw=g&hvrand=3126569913376291643&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9071400&hvtargid=pla-1025753890035&psc=1) 

This chapter is my notes.


## What is DAX?

DAX stands for "Data Analysis Expressions". It is the native formula and query language for Microsoft PowerPivot, Power BI Desktop and SQL Server Analysis Services Tabular models.


## Useful websites for using DAX?
[DAX.do](https://dax.do/) is a playground to write and run DAX queries.

[DAXformatter](https://www.daxformatter.com/) is a very useful tool to format DAX code.

## My own DAX notes
When I first started using DAX, it felt intuitive but also mysterious at the same time. Very often, it just worked miraculously. After battling with it for a year, I decided to read the DAX guide as opposed to relying on my instinct. Understanding the evaluation contexts is the key to unlocking the full power of the DAX language. Here is the most important thing to note.

```{note}
The filter context filters the model; the row context iterates a table.
```
However, **CALCULATE** can transform a row context into a filter context. Context transition is invoked whenever there is a row context. For example, if one uses **Calculate** in a calculated column, context transition occurs.


### Using a role

Roles are very similar to directives, but they are less-complex and written
entirely on one line. You can insert a role into your book's content with
this pattern:

```
Some content {rolename}`and here is my role's content!`
```

Again, roles will only work if `rolename` is a valid role's name. For example,
the `doc` role can be used to refer to another page in your book. You can
refer directly to another page by its relative path. For example, the
role syntax `` {doc}`intro` `` will result in: {doc}`intro`.

For more information on writing roles, see the
[MyST documentation](https://myst-parser.readthedocs.io/).


### Adding a citation

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

````
```{bibliography}
```
````

Resulting in a rendered bibliography that looks like:

```{bibliography}
```


### Executing code in your markdown files

If you'd like to include computational content inside these markdown files,
you can use MyST Markdown to define cells that will be executed when your
book is built. Jupyter Book uses *jupytext* to do this.

First, add Jupytext metadata to the file. For example, to add Jupytext metadata
to this markdown page, run this command:

```
jupyter-book myst init markdown.md
```

Once a markdown file has Jupytext metadata in it, you can add the following
directive to run the code at build time:

````
```{code-cell}
print("Here is some code to execute")
```
````

When your book is built, the contents of any `{code-cell}` blocks will be
executed with your default Jupyter kernel, and their outputs will be displayed
in-line with the rest of your content.

For more information about executing computational content with Jupyter Book,
see [The MyST-NB documentation](https://myst-nb.readthedocs.io/).
