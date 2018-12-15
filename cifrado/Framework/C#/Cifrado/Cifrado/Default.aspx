<%@ Page Title="**Cifrado en c#**" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Cifrado._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">

    <h1>*** Cifrados ***</h1>
   
    <label>Ingrese texto a cifrar: </label>
    <br />
    <textarea rows="4" cols="40"></textarea>

    <table>
        <tbody>
            <tr>
                <th>
                    <h1>Cifrado cesar: </h1>
                    <br />
                    <label>Ingrese desplazamiento: </label>
                    <br />
                    <input type="number" min="0"/>
                    <br />
                    <label>Texto cifrado</label>
                    <br />
                    <textarea rows="4" cols="40"></textarea>
                </th>
            </tr>


            <tr>
                <th>
                    <h1>Cifrado por transposicion</h1>
                    <br />
                    <label>Texto cifrado</label>
                    <br />
                    <textarea rows="4" cols="40"></textarea>
                </th>
            </tr>


            <tr>
                <th>
                    <h1>Cifrado por transposicion en grupos</h1>
                    <br />
                    <input type="number" min="0"/>
                    <br />
                    <label>Texto cifrado</label>
                    <br />
                    <textarea rows="4" cols="40"></textarea>
                </th>
            </tr>

        </tbody>
    </table>

</asp:Content>
