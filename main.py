def printLightHouse(arr, n):
    '''
    입력 배열이 [5,2,1,3]이라 하면
    5는 자기 좌즉에 자신보다 큰수가 없으므로 -1,
    2는 좌측에 첫번째로 나타나는 자신보다 큰 수가 5이므로 5의 인덱스 0을 출력
    1은 좌측에 첫번째로 나타나는 자신보다 큰 수가 2이므로 2의 인덱스 1을 출력
    3은 좌측에 첫번째로 나타나는 자신보다 큰 수가 5이므로 5의 인덱스 0을 출력
    따라서 result=[-1,0,1,0]
    '''

    # 빈 스택 생성
    result = list()
    S = list()
    R = list()

    # arr의 원소를 하나씩 돌아감
    for i in range(n):

        # S에서 원소를 하나씩 제거함. S[-1]이 arr[i]보다 커지는 순간까지 제거함
        while (len(S) > 0 and S[-1] <= arr[i]):
            S.pop()
            R.pop()

        # 초기조건이거나 자기 자신의 좌측의 모든 원소보다 큰 원소의 경우
        if (len(S) == 0):
            result.append(-1)

        else:  # S의 모든원소가 제거되지 않고 while이 끝난경우
            # larger element
            # result.append(i-1)
            result.append(R[-1])

        S.append(arr[i])
        R.append(i)
        # print(R)
        # print(S)
    print(result)


# Driver Code
# arr = [ 5, 3, 1, 6, 4]
# arr = [ 5, 4, 3, 2, 1]
# arr = [ 1, 2, 3, 4, 5]
# arr = [ 1, 2, 1, 2, 1]
arr = [5, 2,1,3]
n = len(arr)
printLightHouse(arr, n)
