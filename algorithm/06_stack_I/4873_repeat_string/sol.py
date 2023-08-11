import sys
sys.stdin = open('input.txt')


def search(word):
    tmp = '' # 다음 조사 대상이 될 문자열

    # 조사 대상 문자와 조사 대상 다음 문자가
    # 같은지를 알아 보고,
        # 같으면 다음 조사 대상에서 두 글자 모두 제외
        # 다르면, 현재 조사대상인 문자는 다음 조사 대상에 포함
            # 그리고, 조사 대상을 다음칸으로 이동
    # 조사 대상 index
    idx = 0
    while idx < len(word)-1:
        if word[idx] == word[idx+1]:
            tmp += word[idx+2:] # idx, idx+1 번째 뺴고 전부 추가
            word = tmp
            # print(tmp, word)
            idx = 0
            tmp = ''
            # break
        else:
            tmp += word[idx]    # 다음 조사 대상에 현재 문자 추가
            idx += 1            # 조사 위치 변경
        # print(tmp, idx)
    return word

T = int(input())

for tc in range(1, T+1):
    word = input()
    # print(word)
    print(f'#{tc} {len(search(word))}')
