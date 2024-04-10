#include <bits/stdc++.h>
using namespace std;

int a[100001];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    sort(a + 1, a + 1 + n);
    for (int i = 1; i <= n; i++)
    {
        if (i != 1)
        {
            cout << " ";
        }
        cout << a[i];
    }
    return 0;
}