# resume

Since my resume is in HTML, I can treat it as a software project and apply standard practices to it.
Most importantly check dead links periodically!

Here are the checks I have in mind so far:

1. Nightly tests:, I have [weekly job](https://github.com/diaasami/resume/actions/workflows/weekly.yml) to [check dead links](https://github.com/diaasami/resume/blob/master/check_resume_links.py).
2. Pre-commit job to check structure and spelling (WIP)
3. Deploy: Create PDF from tags (WIP)