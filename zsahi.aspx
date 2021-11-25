<%@ Page Language="C#" Debug="true" Trace="false" %>
<%@ Import Namespace="System.Diagnostics" %>
<%@ Import Namespace="System.IO" %>
<script Language="c#" runat="server">
void Page_Load(object sender, EventArgs e)
{
    output_text.Text= "<h1 style='color:red'>Computer Name: " + System.Environment.GetEnvironmentVariable("COMPUTERNAME") +"<br>";
    output_text.Text += "Username: " + Environment.UserName + "<br>";  
    output_text.Text += "IP Address: " + Request.ServerVariables["LOCAL_ADDR"]; 
}
</script>
<HTML>
<HEAD>
<title>POC Here</title>
</HEAD>
<body >
<asp:Label id="output_text" runat="server"></asp:Label>
</body>
</HTML>