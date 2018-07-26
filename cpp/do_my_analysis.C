#include <string>

using std::string;

void do_my_analysis(const char * arg = "default.root")
{
  gROOT->ProcessLine(".L tree.C+O");
  string line = string("do_analysis(\"") + string(arg) + string("\");");
  gROOT->ProcessLine(line.c_str());
}
