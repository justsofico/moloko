from scanner import Scanner

from duplicate_finder import DuplicateFinder

from report import show

documents = Scanner().scan()

groups = DuplicateFinder().find(

    documents

)

show(

    documents,

    groups

)
