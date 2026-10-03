#!/usr/bin/env python3
"""
transform_characters.py
Replaces the female character in the Architect card and Off-The-Clock runner
with the canonical male cartoon character representing Subhajit Kar.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ABOUT_SVG = ROOT / "assets/about-life.svg"

def transform_architect_card(svg_text: str) -> str:
    print("  Transforming Architect Card character to male Subhajit Kar...")
    
    # 1. Recolor clothes in av_i48 (female pink sweater -> male tech hoodie)
    # Pink sweater light: #f95dd2 -> #2b3658 (hoodie highlight/crease)
    # Pink sweater mid:   #f939c9 -> #1c2440 (hoodie main slate/navy)
    # Pink sweater dark:  #d41ece -> #12182b (hoodie deep shadow)
    
    # Also in av_i48, let's add subtle cyan drawstring / tech collar accent
    # First, let's find the av_i48 section
    av_i48_m = re.search(r'(<g transform=\"matrix\(1,0,0,1,532,398\)\" id=\"av_i48\">.*?</g></g></g></g></g></g>)', svg_text, re.DOTALL)
    if not av_i48_m:
        print("  ⚠️ Could not find av_i48 block!")
        return svg_text
    
    av_i48_content = av_i48_m.group(0)
    av_i48_mod = av_i48_content.replace('#f95dd2', '#2e3b63')
    av_i48_mod = av_i48_mod.replace('#f939c9', '#1d2644')
    av_i48_mod = av_i48_mod.replace('#d41ece', '#11172a')
    
    # Add subtle cyan tech hoodie drawstrings/collar trim
    hoodie_accents = '''
      <!-- Male Tech Hoodie Drawstrings & Accent Trim -->
      <path d="M-195,-50 Q-192,-20 -188,15" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".85"/>
      <circle cx="-188" cy="16" r="2.2" fill="#22d3ee"/>
      <path d="M-175,-52 Q-170,-22 -165,10" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".85"/>
      <circle cx="-165" cy="11" r="2.2" fill="#22d3ee"/>
    '''
    # Insert accents right before the closing tag of av_i48
    last_g = av_i48_mod.rfind('</g>')
    if last_g != -1:
        av_i48_mod = av_i48_mod[:last_g] + hoodie_accents + av_i48_mod[last_g:]
    
    svg_text = svg_text.replace(av_i48_content, av_i48_mod)
    
    # 2. Transform av_i50 (head, hair, face)
    # Female hair colors: #0d014a, #120070, #130751, #0a003d -> male hair #0a0d18, #141a2e, #1c2440
    av_i50_m = re.search(r'(<g id=\"av_i50\">.*?</g></g></g></g></g></g></g>)', svg_text, re.DOTALL)
    if not av_i50_m:
        print("  ⚠️ Could not find av_i50 block!")
        return svg_text
    
    av_i50_content = av_i50_m.group(0)
    av_i50_mod = av_i50_content
    
    # Remove the swinging ponytail group
    # <g><g transform="translate(-199.5,-282.5)"><g transform="rotate(0)"><animateTransform repeatCount="indefinite" ... <path fill="#0d014a" d="M-163.9,-278.4...
    ponytail_regex = r'<g><g transform=\"translate\(-199\.5,-282\.5\)\">.*?</g></g></g></g>'
    av_i50_mod = re.sub(ponytail_regex, '', av_i50_mod, flags=re.DOTALL)
    
    # Recolor hair from purple/violet to short black/dark charcoal
    av_i50_mod = av_i50_mod.replace('#0d014a', '#0b0e1a')
    av_i50_mod = av_i50_mod.replace('#120070', '#12182b')
    av_i50_mod = av_i50_mod.replace('#130751', '#182038')
    av_i50_mod = av_i50_mod.replace('#0a003d', '#080a14')
    
    # Add modern architect glasses and short hair refinement over the head group
    # Eye coordinates: left eye ~ (-185, -216), right eye ~ (-125, -210)
    male_head_additions = '''
      <!-- Modern Architect Glasses (Subhajit Kar signature) -->
      <g id="male_glasses" opacity=".95">
        <!-- Left Frame -->
        <rect x="-198" y="-228" width="34" height="23" rx="7" fill="#080a14" fill-opacity=".3" stroke="#22d3ee" stroke-width="2"/>
        <path d="-194 -222 L -186 -222" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" opacity=".6"/>
        <!-- Right Frame -->
        <rect x="-142" y="-222" width="34" height="23" rx="7" fill="#080a14" fill-opacity=".3" stroke="#22d3ee" stroke-width="2"/>
        <path d="-138 -216 L -130 -216" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" opacity=".6"/>
        <!-- Bridge -->
        <path d="M-164,-218 Q-153,-222 -142,-214" stroke="#22d3ee" stroke-width="2.2" stroke-linecap="round" fill="none"/>
        <!-- Temple Arm to ear -->
        <path d="M-198,-220 Q-216,-212 -234,-202" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" fill="none"/>
      </g>
      <!-- Masculine short hair top & taper cut overlay -->
      <path d="M-225,-265 Q-215,-315 -165,-315 Q-115,-315 -95,-285 Q-85,-260 -92,-230 Q-105,-220 -115,-250 Q-150,-290 -210,-260 Z" fill="#0b0e1a"/>
      <path d="M-195,-305 Q-160,-318 -125,-300 Q-150,-305 -180,-295 Z" fill="#2e3b63" opacity=".6"/>
    '''
    
    last_g_50 = av_i50_mod.rfind('</g>')
    if last_g_50 != -1:
        av_i50_mod = av_i50_mod[:last_g_50] + male_head_additions + av_i50_mod[last_g_50:]
        
    svg_text = svg_text.replace(av_i50_content, av_i50_mod)
    return svg_text

def transform_fitness_runner(svg_text: str) -> str:
    print("  Transforming Off-The-Clock Runner to male Subhajit Kar...")
    
    # 1. Slide 0 contains the runner SVG: <svg x="748" y="148" width="444" height="312" viewBox="170 60 740 900" ...
    slide0_m = re.search(r'(<g class=\"slide\" opacity=\"1\" style=\"animation-delay:0s\"><svg x=\"748\" y=\"148\" width=\"444\" height=\"312\" viewBox=\"170 60 740 900\".*?</svg></g>)', svg_text, re.DOTALL)
    if not slide0_m:
        print("  ⚠️ Could not find Slide 0 block!")
        return svg_text
        
    slide0_content = slide0_m.group(0)
    slide0_mod = slide0_content
    
    # A. Remove ponytail (CHILD 12):
    # <g id="jg_i0"><g transform="translate(549,412.7)"><animateTransform ... <path fill="#5b3b28" d="M-143.1,-171.4...
    ponytail_runner_regex = r'<g id=\"jg_i0\"><g transform=\"translate\(549,412\.7\)\"><animateTransform repeatCount=\"indefinite\" type=\"translate\" attributeName=\"transform\" dur=\"1s\" begin=\"0s\" calcMode=\"spline\" values=\"549 412\.7; 569 502; 519 498\.7; 579 412\.7; 569\.3 502; 519 498\.7; 549 412\.7\".*?<path fill=\"#5b3b28\".*?</path></g></g></g></g></g></g></g></g>'
    # Let's replace the ponytail with empty or male short hair back
    slide0_mod = re.sub(ponytail_runner_regex, '<!-- Ponytail Removed for Male Character -->', slide0_mod, flags=re.DOTALL)
    
    # B. Hair & Head (CHILD 13):
    # Hair was brown #5b3b28 -> change to black/dark charcoal #0b0e1a
    # Hair band was #5a9ebc -> change to #0b0e1a
    # Also adjust female hair shapes
    slide0_mod = slide0_mod.replace('#5b3b28', '#0b0e1a')
    slide0_mod = slide0_mod.replace('#221914', '#080a14')
    
    # C. Running Shirt (Torso):
    # Currently female teal top #5a9ebc -> change to high-perf cyan #22d3ee & deep navy #161c2e
    # In Child 7, 9, 11:
    slide0_mod = slide0_mod.replace('#5a9ebc', '#22d3ee')
    
    # D. Running Shorts:
    # #2f2f48 -> deep athletic navy #161c2e
    # #5c5c7e -> athletic navy highlight #222b44
    slide0_mod = slide0_mod.replace('#2f2f48', '#161c2e')
    slide0_mod = slide0_mod.replace('#5c5c7e', '#222b44')
    
    svg_text = svg_text.replace(slide0_content, slide0_mod)
    return svg_text

def main():
    print("🎨 Executing Precise Character Replacement in assets/about-life.svg...")
    with open(ABOUT_SVG, "r", encoding="utf-8") as f:
        svg_text = f.read()
        
    svg_text = transform_architect_card(svg_text)
    svg_text = transform_fitness_runner(svg_text)
    
    with open(ABOUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_text)
        
    print("✅ Successfully updated assets/about-life.svg with Male Subhajit Kar character!")

if __name__ == "__main__":
    main()
