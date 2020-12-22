
st = {'breakfast', 'lunch', 'dinner', 'breakfast', 'lunch', 'dinner'}
st2 = {'breakfast', 'lunch', 'dinner', 'night snack'}
print(st)
print(st2)

st.add('lunch snack')  # stに新たな値を追加
st.copy()  # stをコピー(新たな変数に割り当て可能)
st.difference(st2)  # stの値の中でst2にない値を特定
st.difference_update(st2)  # st, st2共通の値をstから削除
st.intersection(st2)  # 新たなsetにst, st2共通の値を追加(割り当て可能)
st.intersection_update(st2)  # st, st2共通ではない値をstから削除
st.isdisjoint(st2)  # st, st2共通の値があるかを判別(True/False)
st.issubset(st2)  # stがst2に含まれるかを判別(True/False)
st.issuperset(st2)  # stがst2を含むかを判別(True/False)
st.symmetric_difference(st2)  # 新たなsetにst, st2共通ではない値を追加(割り当て可能)
st.symmetric_difference_update(st2)  # stからst, st2共通の値を削除し、st, st2共通ではない値を追加
st.union(st2)  # 新たなsetにst, st2の値を追加(setのなので重複は削除)
st.update(st2)  # stにst2の値を追加(setのなので重複は削除)

# popでrandomに値が消去されるので、下の値は一意的ではありません
# popでlunchが消去された場合エラーが生じます
st.pop()  # stからrandomに値を削除
st.remove('lunch')  # 'lunch'を削除(lunchがない場合エラーが生じる)
st.discard('lunch')  # 'lunch'を削除(lunchがなくてもエラーは生じない)
st.clear()  # 全ての値を削除
