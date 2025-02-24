
## WINE
%%[[2025-02-21]] @ 16:10%%

C:\users\joeashton\AppData\Local\Didactic\FluidSIM6

![](Getting%20FluidSIM%20Working%20-%20initial%20registry%20key%20error.png)

I don't know what registry keys to change, I could Install it on my windows VM and compare.

I've tried installing in the full windows virtual machine and got the exact same error.

I think it's to do with the .NET 4.7 dependency, and I can't get around that as it's still broken on WINE.

## Virtualisation & window pass through
%%[[2025-02-21]] @ 20:15%%

I've installed it inside my QEMU Windows VM and I've set up [Winapps](https://github.com/Fmstrat/winapps?tab=readme-ov-file) to do single window pass through.

I've also gone out my way to moc up the logo and a info file for it. Once I've added the MIMETYPEs I'll send it as a pull to the public repo so other users can have it work by default.

