
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

const int sizen = 4;

long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];
long long dpA[sizen][sizen], dpB[sizen][sizen], dpB_transposed[sizen][sizen];
long long sumRow[sizen];

long long productMat[sizen][sizen];

//Simple recursion  which returns the minimum cost of going from i,j to n,n
long long FindMinCostA(int i, int j, int n)
{
    /*
    //going out of bounds
    if (i >= n)
        return 0;
    //going out of bounds
    if (j >= n)
        return 0;
    //reaching the last cell
    if (i == n - 1 && j == n - 1)
        return costMatrixA[i][j];
    //going down or right
    return costMatrixA[i][j] + min(FindMinCostA(i + 1, j, n), FindMinCostA(i, j + 1, n));
     */

    return dpA[i][j];
}
//Simple recursion which returns the maximum cost of going from i,j to n,n
long long FindMaxCostB(int i, int j, int n)
{
    /*
    //going out of bounds
    if (i >= n)
        return 0;
    //going out of bounds
    if (j >= n)
        return 0;
    //reaching the last cell
    if (i == n - 1 && j == n - 1)
        return costMatrixB[i][j];
    //going down or right
    return costMatrixB[i][j] + max(FindMaxCostB(i + 1, j, n), FindMaxCostB(i, j + 1, n));
    */

    return dpB[j][i];
}

void calculate() {
    dpA[sizen - 1][sizen - 1] = costMatrixA[sizen - 1][sizen - 1];
    dpB[sizen - 1][sizen - 1] = costMatrixB[sizen - 1][sizen - 1];
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (i == n - 1 && j == n - 1) {
                continue;
            } else if (i == n - 1) {
                dpA[i][j] = dpA[i][j + 1] + costMatrixA[i][j];
                dpB[i][j] = dpB[i][j + 1] + costMatrixB[i][j];
            } else if (j == n - 1) {
                dpA[i][j] = dpA[i + 1][j] + costMatrixA[i][j];
                dpB[i][j] = dpB[i + 1][j] + costMatrixB[i][j];
            } else {
                dpA[i][j] = min(dpA[i + 1][j], dpA[i][j + 1]) + costMatrixA[i][j];
                dpB[i][j] = min(dpB[i + 1][j], dpB[i][j + 1]) + costMatrixB[i][j];
            }
            dpB_transposed[j][i] = dpB[i][j];
        }
    }


}

int main()
{
    calculate();
    int i, j, k;
    srand(time(0));
    // initialisation
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            costMatrixA[i][j] = 1 + rand() % 10;
            costMatrixB[i][j] = 1 + rand() % 10;
            productMat[i][j] = 0;
        }
    }
    //creating productMat as explained in the beginning
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            for (k = 0; k < sizen; k++)
                productMat[i][j] += FindMinCostA(i, k, sizen) * FindMaxCostB(k, j, sizen);
            sumRow[i] += productMat[i][j];
        }
    }
    //filter of size 4 x n
    long long filterArray[4][sizen];
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }
    // matrix of dimension (sizen/c) x 1 where c = 4
    long long finalMat[sizen / 4];
    // applying the filter
    for (i = 0; i < sizen - 4; i += 4)
    {
        long long sum = 0;
        // dot product of 4xn portion of productMat
        //for (j = 0; j < sizen; j++)
        //{
            for (int filterRow = 0; filterRow < 4; filterRow++)
            {
                sum += sumRow[i + filterRow];
            }
        //}
        finalMat[i / 4] = sum;
    }

    return 0;
}