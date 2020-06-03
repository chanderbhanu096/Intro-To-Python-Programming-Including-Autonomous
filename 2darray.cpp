#include <iostream>
#include <vector>
using namespace std;
int main ()
{

  vector < vector < int >> vector2(5,vector <int>(4,4));



  for (int i = 0; i < vector2.size (); i++)
    {
      for (int j = 0; j < vector2[0].size (); j++)
	{
	  cout << vector2[i][j] << " ";
	}
	  cout << "hello";
      cout << endl;
    }

  return 0;
}
