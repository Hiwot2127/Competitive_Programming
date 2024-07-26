func luckyNumbers (matrix [][]int) []int {
    luckyNumbers := []int{}

    for i := 0; i < len(matrix); i++ {
        minRowValue := matrix[i][0]
        minColIndex := 0
        for j := 1; j < len(matrix[i]); j++ {
            if matrix[i][j] < minRowValue {
                minRowValue = matrix[i][j]
                minColIndex = j
            }
        }
        isMaxInColumn := true
        for k := 0; k < len(matrix); k++ {
            if matrix[k][minColIndex] > minRowValue {
                isMaxInColumn = false
                break
            }
        }
        if isMaxInColumn {
            luckyNumbers = append(luckyNumbers, minRowValue)
        }
    }
    return luckyNumbers
}