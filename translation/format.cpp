#include <iostream>
#include <ios>
#include <string>
#include <fstream>

int main ()
{
  std::fstream myfile;
  std::string line;

  myfile.open("train.jsonl", std::ios::out | std::ios::in);

  while (!myfile.eof())
  {
    std::getline(myfile,line); // Check getline() doc, you can retrieve a line before/after a given string etc.
    std::cout << line << '\n';
    //if (line == something)
    //{
        // do stuff with line, like checking for content etc.
    //}
  }
  myfile.close();
  return 0;
}