// { Driver Code Starts
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;



/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


 // } Driver Code Ends

class Solution
{
    public:
    void merge(int arr[], int l, int m, int r)
    {
         int n1,n2,i,j,k;
         n1=m-l+1;
         n2=r-m;
         i=0;
         j=0;
         k=l;
         int temp[n1];
         int temp2[n2];
         
         for(int z=0;z<n1;z++){
             temp[z]=arr[l+z];
         }
         
         for(int z=0;z<n2;z++){
             temp2[z]=arr[m+1+z];
         }
         
         
         while(i<n1 && j<n2){
             
             if(temp[i]<temp2[j]){
                 arr[k]=temp[i];
                 i++;
                 k++;
             }
             else{
                 arr[k]=temp2[j];
                 j++;
                 k++;
             }
             
             //cout<<"he"<<" ";
         }
         
         while(i<n1){
             arr[k]=temp[i];
             i++;k++;
             //cout<<k<<"hey"<<" ";
         }
         
         while(j<n2){
             arr[k]=temp2[j];
             j++;k++;
            // cout<<k<<"hello"<<" ";
         }
         
         
    }
    public:
    void mergeSort(int arr[], int l, int r)
    {
        if(l>=r){return;}
        int m=l+(r-l)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
};

// { Driver Code Starts.


int main()
{
    int n,T,i;

    scanf("%d",&T);

    while(T--){
    
    scanf("%d",&n);
    int arr[n+1];
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);

    Solution ob;
    ob.mergeSort(arr, 0, n-1);
    printArray(arr, n);
    }
    return 0;
}  // } Driver Code Ends