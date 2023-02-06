Sub generate_unknown_excel_results()
Dim ac As Double
Dim ah As Double
Dim hri As Double
Dim i As Integer
Dim index As Integer
Dim long_string_result As String

ac = 0
ah = 0
hri = 0
i = 2

Dim LDSI_interpolated_results() As Variant
Dim CDSI_interpolated_results() As Variant
Dim LDSE_interpolated_results() As Variant
Dim CDSE_interpolated_results() As Variant

Application.Calculation = xlCalculationManual
Sheets.Add.Name = "unknown_results"
Cells(1,1) = "ac,ah,hri,LDSI_i0_depth,LDSI_i0_surface,LDSI_i1_depth,LDSI_i1_surface,LDSI_i2_depth,LDSI_i2_surface,LDSI_i3_depth,LDSI_i3_surface,CDSI_i0_depth,CDSI_i0_surface,CDSI_i1_depth,CDSI_i1_surface,CDSI_i2_depth,CDSI_i2_surface,CDSI_i3_depth,CDSI_i3_surface,LDSE_i0_depth,LDSE_i0_surface,LDSE_i1_depth,LDSE_i1_surface,LDSE_i2_depth,LDSE_i2_surface,LDSE_i3_depth,LDSE_i3_surface,CDSE_i0_depth,CDSE_i0_surface,CDSE_i1_depth,CDSE_i1_surface,CDSE_i2_depth,CDSE_i2_surface,CDSE_i3_depth,CDSE_i3_surface"
Worksheets("FCG").Activate

Do Until ac > 1.03
    'row, column, index start at 1
    Cells(27, 4) = ac
    ah = 0
    Do Until ah > 0.83
        Cells(25, 4) = ah
        hri = 0
        Do Until hri > 1.03
            
            long_string_result = ""
            
            Cells(23, 4) = hri
            
            Calculate
            
            LDSI_interpolated_results = Range("D30:D37")
            CDSI_interpolated_results = Range("D39:D46")
            LDSE_interpolated_results = Range("D48:D55")
            CDSE_interpolated_results = Range("D57:D64")
            
            long_string_result = CStr(ac) & "," & CStr(ah) & "," & CStr(hri)
            
            For index = 1 To UBound(LDSI_interpolated_results)
                long_string_result = long_string_result & "," & CStr(LDSI_interpolated_results(index, 1))
            Next index
            
            For index = 1 To UBound(CDSI_interpolated_results)
                long_string_result = long_string_result & "," & CStr(CDSI_interpolated_results(index, 1))
            Next index
            
            For index = 1 To UBound(LDSE_interpolated_results)
                long_string_result = long_string_result & "," & CStr(LDSE_interpolated_results(index, 1))
            Next index
            
            For index = 1 To UBound(CDSE_interpolated_results)
                long_string_result = long_string_result & "," & CStr(CDSE_interpolated_results(index, 1))
            Next index
            
            Worksheets("unknown_results").Cells(i, 1) = long_string_result
            
            hri = hri + 0.05
            hri = Round(hri, 2)
            i = i + 1
        Loop
        ah = ah + 0.05
        ah = Round(ah, 2)
        
        If ah = 0.8 Then
            ah = 0.799999
        End If
    Loop
    ac = ac + 0.05
    ac = Round(ac, 2)
Loop

ActiveWorkbook.Save

End Sub