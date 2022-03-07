def findLeftMostNumber(Array, n):
    '''
    출력 배열의 i번째 배열은 입력 배열의 i번째 원소 기준으로 왼쪽으로 입력 배열의 i번째 원소보다 큰 첫번째 원소의 인덱스이다.
    배열에는 같은 수가 절대 존재하지 않는다. 
    배열에는 항상 1보다 크거나 같은 자연수가 온다.
    예시)
    입력 배열이 [5,2,1,3]이라 하면
    5는 자기 좌즉에 자신보다 큰수가 없으므로 -1,
    2는 좌측에 첫번째로 나타나는 자신보다 큰 수가 5이므로 5의 인덱스 0을 출력
    1은 좌측에 첫번째로 나타나는 자신보다 큰 수가 2이므로 2의 인덱스 1을 출력
    3은 좌측에 첫번째로 나타나는 자신보다 큰 수가 5이므로 5의 인덱스 0을 출력
    따라서 Result=[-1,0,1,0]
    '''

    # 빈 스택 생성
    Result = list()
    Value = list()
    Index = list()

    # arr의 원소를 하나씩 돌아감
    for i in range(n):

        # S에서 원소를 하나씩 제거함. S[-1]이 arr[i]보다 커지는 순간까지 제거함
        while (len(Value) > 0 and Value[-1] <= Array[i]):
            Value.pop()
            Index.pop()

        # 초기조건이거나 자기 자신의 좌측의 모든 원소보다 큰 원소의 경우
        if (len(Value) == 0):
            Result.append(-1)

        else:  # Value 의 모든원소가 제거되지 않고 while이 끝난경우
            # larger element
            # result.append(i-1)
            Result.append(Index[-1])

        Value.append(Array[i])
        Index.append(i)
        # print(Index)
        # print(Value)
    print(Result)


# 예시 코드
# Array = [ 5, 3, 1, 6, 4]
# Array = [ 5, 4, 3, 2, 1]
# Array = [ 1, 2, 3, 4, 5]
# Array = [ 1, 2, 1, 2, 1]
Array = [5, 2, 1, 3]
n = len(Array)
findLeftMostNumber(Array, n)
