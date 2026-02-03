# How to Update Your Team Profile

This guide will help you update your profile information on the ADS/SciX website.

## Quick Links

- **Your bio content**: `_includes/_teambios/[your-id].md`
- **Your profile page**: `about/team/team/[your-id].md`
- **Team data file**: `_data/team.yml`

Replace `[your-id]` with your identifier (e.g., `mpolimera`, `aaccomazzi`, etc.)

---

## What You Can Update

### 1. Your Bio and Photo

**Location**: `_includes/_teambios/[your-id].md`

**What's in this file:**
- Your photo (image path)
- Your biography text
- Your email address
- Links to your personal website or social media

**Example** (`_includes/_teambios/mpolimera.md`):
```markdown
<img src="{{ site.baseurl }}/about/team/img/mpolimera.jpg" height="200" width="200" alt="Image" style="float: left; margin: 4px 10px 0px 0px; border: 1px solid #000000;">

Mugdha received her Ph.D. in Astrophysics from the University of North Carolina...

[mugdha.polimera [at] cfa.harvard.edu](mailto:mugdha.polimera@cfa.harvard.edu)
```

**To update:**
1. Navigate to `_includes/_teambios/`
2. Find your file (e.g., `mpolimera.md`)
3. Edit your bio text, photo path, or email
4. Save the file

**To update your photo:**
1. Add your new photo to `about/team/img/`
2. Name it `[your-id].jpg` (e.g., `mpolimera.jpg`)
3. Update the image path in your bio file if needed

### 2. Your Job Title (Subtitle on Profile Page)

**Location**: `about/team/team/[your-id].md`

**What's in this file:**
- Your name (title)
- Your job title (subtitle)
- A reference to your bio file

**Example** (`about/team/team/mpolimera.md`):
```yaml
---
layout: about
title: "Dr. Mugdha Polimera"
subtitle: "Back-End Development & Astrophysicist"
---

{% include _teambios/mpolimera.md %}
```

**To update your job title:**
1. Navigate to `about/team/team/`
2. Find your file (e.g., `mpolimera.md`)
3. Edit the `subtitle:` line
4. Save the file

⚠️ **Note**: This only updates your individual profile page. To update your title on the team index pages, see section 3 below.

### 3. Your Job Title on Team Index Pages

**Location**: `_data/team.yml`

The team index pages (both ADS and SciX) automatically pull job titles from this central file.

**Example entry**:
```yaml
- id: mpolimera
  name: "Dr. Mugdha Polimera"
  title_ads: "Back-End Development & Astrophysicist"
  title_scix: "Back-End Development"
  order: 19
```

**To update your job title on index pages:**
1. Navigate to `_data/team.yml`
2. Find your entry (search for your `id`)
3. Edit `title_ads` (for ADS pages) or `title_scix` (for SciX pages)
4. Save the file

✅ **Automatic update**: Your title will appear on both `about/team/index.md` and `scixabout/team/index.md` automatically!

**Fields explained:**
- `id`: Your unique identifier (don't change this)
- `name`: Your full name with title
- `title_ads`: Your job title on the ADS website
- `title_scix`: Your job title on the SciX website
- `order`: Your position in the team list (don't change without coordinating)
- `role_type`: Your role category (only for special roles like research associates)

---

## Common Tasks

### Update My Biography
1. Go to `_includes/_teambios/[your-id].md`
2. Edit the text
3. Save

### Change My Photo
1. Add new photo to `about/team/img/[your-id].jpg`
2. If using a different filename, update the image path in `_includes/_teambios/[your-id].md`
3. Save

### Update My Job Title
**For your profile page only:**
1. Edit `about/team/team/[your-id].md`
2. Change the `subtitle:` line
3. Save

**For team index pages:**
1. Edit `_data/team.yml`
2. Find your entry and update `title_ads` or `title_scix`
3. Save

### Update My Email Address
1. Go to `_includes/_teambios/[your-id].md`
2. Find the email line at the bottom
3. Update both the display text and the `mailto:` link
4. Save

---

## File Structure Overview

```
adsabs.github.io/
├── _data/
│   └── team.yml                    ← Team job titles for index pages
├── _includes/
│   └── _teambios/
│       ├── mpolimera.md           ← Your bio content
│       ├── aaccomazzi.md
│       └── [other team members]
├── about/
│   └── team/
│       ├── img/
│       │   ├── mpolimera.jpg      ← Your photo
│       │   └── [other photos]
│       └── team/
│           ├── mpolimera.md       ← Your profile page
│           ├── aaccomazzi.md
│           └── [other profiles]
```

---

## Finding Your Files

### Method 1: Search by Name
Use your IDE's search function (Cmd+P or Ctrl+P) and type your last name.

### Method 2: Find Your ID
Your ID is usually your last name (lowercase). Examples:
- Mugdha Polimera → `mpolimera`
- Alberto Accomazzi → `aaccomazzi`
- Kelly Lockhart → `klockhart`
- Sergi Blanco-Cuaresma → `sblancocuaresma`

Once you know your ID, navigate to:
- Bio: `_includes/_teambios/[your-id].md`
- Profile page: `about/team/team/[your-id].md`

### Method 3: Look in team.yml
1. Open `_data/team.yml`
2. Search for your name (Cmd+F or Ctrl+F)
3. Find your `id` field
4. Use that ID in the paths above

---

## Important Notes

### About Job Titles
You can have **different job titles** in different places:
- **Profile page subtitle**: Customizable, can be unique to you
- **ADS index page**: Pulled from `team.yml` → `title_ads`
- **SciX index page**: Pulled from `team.yml` → `title_scix`

💡 **Tip**: Keep them consistent for clarity, but you can customize if needed!

### About Team Order
The `order` field in `team.yml` determines the order on index pages. If you want to change your position, please coordinate with the web team to avoid conflicts.

### About Photos
- Recommended size: 200x200 pixels
- Format: JPG, PNG, or JPEG
- Keep file sizes reasonable (under 500KB)
- Use professional headshots

### Submitting Your Changes
After making changes:
1. Save all files
2. Commit your changes to a new branch
3. Create a Pull Request (PR) on GitHub
4. Tag @mpolimera or @klockhart for review
5. We'll test your changes and merge if everything looks good!

---

## Need Help?

### Common Issues

**Q: I can't find my bio file**
- Check if your ID is spelled correctly (all lowercase, no spaces)
- Look in `_includes/_teambios/` for all available files

**Q: My job title didn't update on the index page**
- Make sure you edited `_data/team.yml`, not just your profile page
- Check that you saved the file

**Q: My photo isn't showing**
- Check the image path in your bio file
- Make sure the photo exists in `about/team/img/`
- Check the filename matches exactly (case-sensitive)

**Q: I want to add a new section to my bio**
- Edit your bio file (`_includes/_teambios/[your-id].md`)
- Use Markdown formatting
- You can add links, bold text, lists, etc.

### Contact
If you need assistance or have questions about updating your profile, contact:
- Mugdha Polimera
- Kelly Lockhart

---

## For New Team Members

Welcome! Here's how to set up your profile:

### 1. Create Your Bio File
- Create `_includes/_teambios/[your-id].md`
- Copy an existing team member's file as a template
- Update with your information

### 2. Add Your Photo
- Add your photo to `about/team/img/[your-id].jpg`
- Reference it in your bio file

### 3. Create Your Profile Page
- Create `about/team/team/[your-id].md`
- Use this template:
```yaml
---
layout: about
title: "Your Full Name"
subtitle: "Your Job Title"
---

{% include _teambios/[your-id].md %}
```

### 4. Add Yourself to team.yml
- Open `_data/team.yml`
- Add your entry following the format of others
- Choose an appropriate `order` number
- Set `role_type` if you're a research associate or have a special role

### 5. Submit for Review
- Commit your changes to a new branch
- Create a Pull Request (PR) for review
- Tag Mugdha Polimera or Kelly Lockhart for review
- We will test and verify your changes before merging

---

**Last Updated**: February 3, 2026
