# resume

Since my resume is in HTML, I can treat it as a software project and apply standard practices to it.

Most importantly check dead links periodically!



Here are the checks I have in mind so far:

1. Nightly tests: A [weekly job](https://github.com/diaasami/resume/actions/workflows/weekly.yml) to [check dead links](https://github.com/diaasami/resume/blob/master/check_resume_links.py).
1. Pre-commit job to check structure and spelling (WIP)
1. Deploy: Create PDF from tags (WIP)

I believe the same can be done even if the resume is not in HTML:
* Links and text can be extracted from PDFs, links can be checked for validity and text spell-checked.
