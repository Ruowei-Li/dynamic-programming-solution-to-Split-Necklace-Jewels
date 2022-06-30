import sys


def calcMaxVal(a, b):
   if a > b:
      return a
   return b

def calcMaxSumSubSeq(int cirArr[], start, end, n):
   DP = [] * n
   maxSum = 0;
   for i in range (start, end + 1):
      DP[i] = cirArr[i]
      if maxSum < cirArr[i]:
         maxSum = cirArr[i]
   for i in range(start + 2, end + 1):
      for (int j = 0; j < i - 1; j++) {
         if (DP[i] < DP[j] + cirArr[i]) {
            DP[i] = DP[j] + cirArr[i];
            if (maxSum < DP[i])
               maxSum = DP[i];

   return maxSum

int findMaxSum(int cirArr[], int n){
   int maxSumArray1 = calcMaxSumSubSeq(cirArr, 0, (n-2), n);
   int maxSumArray2 = calcMaxSumSubSeq(cirArr, 1, (n-1), n);
   int maxSum = calcMaxVal(maxSumArray1, maxSumArray2);
   return maxSum;
}
int main(){
   int cirArr[] = {4, 1, 5, 3, 2};
   int n = sizeof(cirArr)/sizeof(cirArr[0]);
   cout<<"The maximum sum in circular array such that no two elements are adjacent is "<<findMaxSum(cirArr, n);
   return 0;
}



#content = sys.stdin.readlines()
content = open("input.txt", "r").readlines()
main(content)
