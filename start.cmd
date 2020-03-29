set /p fileName=Input file name:

copy/b .\Videos\* ".\Ready\%fileName%.ts"
del /Q .\Videos\*
pause