import sys#qustndhk gkatnfmf 
inpute = sys.stdin.readline

def solve(n, m):
    return (n-1) + n * (m-1)#초콜릿 짜르기의 사용되는 규칙을 적는다

if __name__ == "__main__": #스크립트 파일이 실행되있는지본다
    n, m = map(int, input().strip().split())
print(solve(n, m))

