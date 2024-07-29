func containsDuplicate(nums []int) bool {
    mapi:=make(map[int]bool)
    for _,num := range nums {
        if mapi[num]{
            return true
        }
        mapi[num]=true
    }
    return false
    }
