# The scenario

We have a client who wants to create a site to display information about courses
taught by various providers. Your task is to create a website that implements the
required features, which can then be delivered to the client. Their operations team 
will be responsible for deploying the site and their developers will be responsible 
for finalising the user experience and maintaining it going forward.

# The Task

We want you to create a site that imports from the provided CSV files. 

4 pages need to be created:

* A home page: this should be a list of course providers, this page should have a filter 
  form as well as being paginated. Each entry should be a link to a provider detail page
* A provider detail page: This should include the provider name and description as well
  as the provider logo if set. There should be a link to the external site if set and a 
  list of the provider courses should be shown.
* A course list page: This should be a list of all courses. This page should have a 
  filter form and be paginated. Each entry should link to the course detail pages.
* A course detail page: This should include the course title and description as well as 
  the provider logo (if set).

The data import should be triggerable from a management command and the admin interface.

`providers.csv` is a list of course providers. 
`courses.csv` contains a list of courses that has a reference to a provider.

You should complete the site in two phases. First add the providers, then add the 
courses.

It is anticipated the work will take 10 hours to complete to a sufficient standard 
that it can be delivered to the client with no further additions.

# Testing

Since this site will be delivered to the client, you should provide tests that verify
everything is working correctly.

# Frontend and styling

We would like you to use any frontend framework you like (Django templates are perfectly fine)
but we would like some styling beyond the default browser styling.

# Submission

To submit your code challenge publish your repo to github (privately) and give [@OmegaDroid](https://github.com/OmegaDroid) and [@StuartMacKay](https://github.com/StuartMacKay) read access.

The code should be runnable with minimal effort. For example, either of these would be fine:

* Running locally using sqlite and a virtual env
* Running in docker with a provided docker-compose file

Please include any instructions in a `README.md`
