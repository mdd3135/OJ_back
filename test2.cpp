#include <bits/stdc++.h>
using namespace std;

int n, a[100001];
void pop_sort()
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j < n; j++)
        {
            if (a[j] > a[j + 1])
            {
                swap(a[j], a[j + 1]);
            }
        }
    }
}
int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    pop_sort();
    for (int i = 1; i <= n; i++)
    {
        if(i != 1) {
            cout << " ";
        }
        cout << a[i];
    }
    return 0;
}
/**
5
4 2 4 5 1

1 2 4 4 5
*/
