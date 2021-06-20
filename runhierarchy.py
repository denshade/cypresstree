import os


def add_successful_run():
    subdir = specfile.replace(".spec.js", "/")
    successspecs.append(specfile)
    if os.path.isdir(subdir): 
        print("run successful. Adding subdirectory " + subdir)
        directories_to_process.append(subdir)


def add_failed_run():
    failedspecs.append(specfile)
    print("Failed, will not run sub branch")

def write_output():
    print("Write to output.html")
    with open("output.html", "w", encoding="utf-8") as text_file:
        text_file.write("<html><head></head><body>")
        for s in specs_that_have_run:
            if s in successspecs: 
                infix = "√"
            else:
                infix = "X"

            text_file.write("<li>" + s +" "+ infix+"</li>")
        text_file.write('</body></html>')


def is_spec_file(file):
    return file.endswith(".spec.js")

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    start_directory = "cypress/integration/basics"
    print("Start running cypress tests from "+ start_directory)
    directories_to_process = [start_directory]
    specs_that_have_run = []
    successspecs = []
    failedspecs = []
    while (len(directories_to_process) > 0):
        current_directory = directories_to_process.pop() 
        for file in os.listdir(current_directory):
            if is_spec_file(file):
                specfile = os.path.join(current_directory, file)
                print("running: "+ specfile)
                retval = os.system('node_modules\.bin\cypress.cmd run -s ' + specfile)
                specs_that_have_run.append(specfile)
                if retval == 0:
                    add_successful_run()
                else:
                    add_failed_run()

    specs_that_have_run.sort()
    write_output()
