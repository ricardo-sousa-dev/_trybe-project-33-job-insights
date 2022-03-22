# -*- coding: utf-8 -*-


from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    list_industries = []
    industries = read(path)
    for industry in industries:
        if industry["industry"] != "":
            if industry["industry"] not in list_industries:
                list_industries.append(industry["industry"])
    return list_industries


def filter_by_industry(jobs, industry):
    jobs_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered.append(job)
    return jobs_filtered


def get_max_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        if salary["max_salary"] != "":
            if salary["max_salary"] not in salaries:
                if salary["max_salary"].isdigit():
                    salaries.append(int(salary["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = []
    for salary in jobs:
        if salary["min_salary"] != "":
            if salary["min_salary"] not in salaries:
                if salary["min_salary"].isdigit():
                    salaries.append(int(salary["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    # https://realpython.com/python-keyerror/
    # https://docs.python.org/3/tutorial/errors.html
    try:
        if job['min_salary'] <= int(salary) <= job['max_salary']:
            return True
        elif job['min_salary'] > job['max_salary']:
            raise ValueError
        else:
            return False
    except(KeyError, TypeError, NameError, ValueError):
        raise ValueError


def filter_by_salary_range(jobs, salary):
    salary_list = []
    for job in jobs:
        try:
            match = matches_salary_range(job, salary)
            if match is True:
                salary_list.append(job)
        except ValueError:
            pass
        # com pass, nada acontece. Similar ao null
        # https://www.programiz.com/python-programming/pass-statement
    return salary_list
