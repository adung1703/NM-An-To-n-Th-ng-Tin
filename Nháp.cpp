#include <iostream>
#include <vector>

using namespace std;

int main() {

    ifstream fread("xargs.1");
    ofstream fwrite("out_xargs.1");

    string content;
    char chr;

    int i = 0;
    while(fread  >> chr){
        content += chr;
    }


    fread.close();
    fwrite.close();

  return 0;
}
