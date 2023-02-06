Sub generate_known_excel_results()
Dim ac As Double
Dim ah As Double
Dim hri As Double
Dim i As Integer
Dim index As Integer
Dim long_string_result As String

Dim ac_list(5) As Double
Dim ah_list(5) As Double
Dim ah_list_display(5) As Double
'FCG spreadsheet throws valueerror when ah = 0.8
'workaround is to pass 0.799999, which returns the correct result anyways
'subsequent processing compares the excel ah value with the python ah value
'and returns differences due to 0.79999 != 0.8
'hence new array with the correct 0.8 defined, which will be passed to the "written" csv
'hence comparison works
Dim hri_list(7) As Double

Dim LDSI_interpolated_results() As Variant
Dim CDSI_interpolated_results() As Variant
Dim LDSE_interpolated_results() As Variant
Dim CDSE_interpolated_results() As Variant

ac_list(0) = 0
ac_list(1) = 0.0625
ac_list(2) = 0.125
ac_list(3) = 0.25
ac_list(4) = 0.5
ac_list(5) = 1

ah_list(0) = 0
ah_list(1) = 0.1
ah_list(2) = 0.2
ah_list(3) = 0.4
ah_list(4) = 0.6
ah_list(5) = 0.7999999

ah_list_display(0) = 0
ah_list_display(1) = 0.1
ah_list_display(2) = 0.2
ah_list_display(3) = 0.4
ah_list_display(4) = 0.6
ah_list_display(5) = 0.8

hri_list(0) = 0
hri_list(1) = 0.0125
hri_list(2) = 0.025
hri_list(3) = 0.05
hri_list(4) = 0.1
hri_list(5) = 0.2
hri_list(6) = 0.5
hri_list(7) = 1

ac = 0
ah = 0
hri = 0
i = 2

Application.Calculation = xlCalculationManual
Sheets.Add.Name = "known_results"
Cells(1,1) = "ac,ah,hri,LDSI_i0_depth,LDSI_i0_surface,LDSI_i1_depth,LDSI_i1_surface,LDSI_i2_depth,LDSI_i2_surface,LDSI_i3_depth,LDSI_i3_surface,CDSI_i0_depth,CDSI_i0_surface,CDSI_i1_depth,CDSI_i1_surface,CDSI_i2_depth,CDSI_i2_surface,CDSI_i3_depth,CDSI_i3_surface,LDSE_i0_depth,LDSE_i0_surface,LDSE_i1_depth,LDSE_i1_surface,LDSE_i2_depth,LDSE_i2_surface,LDSE_i3_depth,LDSE_i3_surface,CDSE_i0_depth,CDSE_i0_surface,CDSE_i1_depth,CDSE_i1_surface,CDSE_i2_depth,CDSE_i2_surface,CDSE_i3_depth,CDSE_i3_surface"
Worksheets("FCG").Activate

Do Until ac = 6
    'row, column, index start at 1
    Cells(27, 4) = ac_list(ac)
    ah = 0
    Do Until ah = 6
        Cells(25, 4) = ah_list(ah)
        hri = 0
        Do Until hri = 8
            
            long_string_result = ""
            
            Cells(23, 4) = hri_list(hri)
            
            Calculate
            
            LDSI_interpolated_results = Range("D30:D37")
            CDSI_interpolated_results = Range("D39:D46")
            LDSE_interpolated_results = Range("D48:D55")
            CDSE_interpolated_results = Range("D57:D64")
            
            long_string_result = CStr(ac_list(ac)) & "," & CStr(ah_list_display(ah)) & "," & CStr(hri_list(hri))
            
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
            
            Worksheets("known_results").Cells(i, 1) = long_string_result
            
            hri = hri + 1
            i = i + 1
        Loop
        ah = ah + 1
        
        If ah = 0.8 Then
            ah = 0.799999
        End If
    Loop
    ac = ac + 1
Loop

ActiveWorkbook.Save

End Sub