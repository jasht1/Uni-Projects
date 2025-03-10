---
category: "literaturenote"
title: "JPK Data Processing Software MANUAL-6.0b"
tags: 
citekey: "jpkinstruments-JPKDataProcessing"
imported: 2025-03-10 03:42
---

# JPK Data Processing Software MANUAL-6.0b


> [!Cite] [jpkinstruments-JPKDataProcessing](zotero://select/library/items/LDM3HXF5)
> [1]  JPK Instruments, Ed., ‘JPK Data Processing Software MANUAL-6.0b’. Burker.
> > [!example]- Metadata    
> > **Title**:: JPK Data Processing Software MANUAL-6.0b
> > **Year**:: Error: `format` can only be applied to dates. Tried for format object
> > **Citekey**:: jpkinstruments-JPKDataProcessing
> > **Sources**:: [Zotero](zotero://select/library/items/LDM3HXF5) [pdf](file:////home/joeashton/Zotero/storage/WYM43XQI/JPK%20Data%20Processing%20Software%20MANUAL-6.0b.pdf) 
> > **FirstEditor**:: JPK Instruments
> > 
> > **itemType**:: document
> > **Publisher**:: Burker

# Annotations

%% begin annotations %%

> [!YellowHighlight] [see in Zotero](zotero://open-pdf/library/items/WYM43XQI?page=72&annotation=3N3CZV7Z)
> "Enabling Offset + Tilt uses the fit  range for a linear fit. This straight line is then subtracted from the whole  curve. Such correction is useful for analysis that is sensitive to small deviations from the baseline, such as calculating the area under the curve."

> [!YellowHighlight] [see in Zotero](zotero://open-pdf/library/items/WYM43XQI?page=75&annotation=B8LZC3UH)
> "The height signal that is derived from the piezo displacement (either from the piezo voltage or the strain gauge measurement) contains both, the distance the cantilever is moved towards the sample and deflection of the cantilever into the opposite direction. But for the application of chain or elasticity fits, plots of force against vertical tip position rather than piezo displacement are needed."

> [!YellowHighlight] [see in Zotero](zotero://open-pdf/library/items/WYM43XQI?page=104&annotation=A6GDRJNT)
> "The original Hertz model was an approximation for the contact and very shallow indentation of two spheres in contact.  (Hertz 1881)."
> > [!note]
> > ![[Contact Mechanics#Spherical contact]]%% end annotations %%

# Notes

%% begin notes %%
### Spherical Contact

#### Force

> [!NOTE] Spherical Contact Force
> $$\LARGE F = \frac{E}{1-v^{2}} \left[ \frac{a^{2}+R^{2}_{s}}{2} \ln \frac{R_{s}+a}{R_{s}-a}  - aR_{s}\right]$$
> 
> Where:
> - $F$ : **Applied force** on the indenter (units: N). This is the force required to indent the material.
> - $E$ : **Young’s modulus** (units: Pa). This represents the stiffness of the indented material.
> - $v$ : **Poisson’s ratio** (dimensionless). It describes how the material deforms laterally when compressed.
> - $a$ : **Contact radius** (units: m). This is the radius of the circular contact area formed between the indenter and the material.
> - $R_s$​ : **Sphere (indenter) radius** (units: m). This is the radius of the spherical indenter pressing into the material.

*from JPK Data Processing Manual.[@jpkinstruments-JPKDataProcessing]*
#### Indentation Depth

> [!INFO] Spherical Contact Indentation Depth
> $$\LARGE \delta = \frac{a}{2} \ln \frac{R_{s}+a}{R_{s}-a}$$
> 
> Where:
> - $\delta$ : **Indentation depth** of the spherical indenter into the material.
> - $a$ : **Contact radius** (units: m). This is the radius of the circular contact area formed between the indenter and the material.
> - $R_s$​ : **Sphere (indenter) radius** (units: m). This is the radius of the spherical indenter pressing into the material.

*from JPK Data Processing Manual.[@jpkinstruments-JPKDataProcessing]*

%% end notes %%

%% Import Date: 2025-03-10T15:42:13.754+00:00 %%
