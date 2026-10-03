#!/usr/bin/env python3
"""
scripts/generate_perfect_fitness_illustrations.py
Generates the 3 organic, professional male fitness illustrations for Subhajit Kar:
1. FOOTBALL (⚽ Male Football Player in striking volley pose)
2. BADMINTON (🏸 Male Badminton Player in airborne jump-smash pose)
3. COOKING (👨‍🍳 Male Lifestyle Chef tossing gourmet ingredients in kitchen)
"""

from pathlib import Path
import xml.etree.ElementTree as ET

def get_subhajit_head(cx, cy, angle_deg=0, looking="down_right", expression="confident", glasses=True):
    """
    Subhajit Kar's canonical 3/4 male head with organic curves:
    - Warm skin tone (#e6a277, shadow #cb7c4d, highlight #fcd9bd)
    - Modern athletic short fade haircut (#0b0e1a with #1e293b texture)
    - Stylish thin dark spectacles with cyan accent (#22d3ee)
    - Masculine jawline, confident eyes, neat trimmed facial hair shadow
    """
    glasses_markup = f'''
        <!-- Modern Rectangular Tech Glasses (3/4 Perspective) -->
        <g id="spectacles" opacity=".95">
          <!-- Near Lens (Larger) -->
          <rect x="{cx - 2}" y="{cy - 12}" width="22" height="15" rx="4" fill="#080c18" fill-opacity=".2" stroke="#0f172a" stroke-width="1.8"/>
          <rect x="{cx - 2}" y="{cy - 12}" width="22" height="15" rx="4" fill="none" stroke="#22d3ee" stroke-width="0.8" stroke-opacity=".8"/>
          <line x1="{cx + 2}" y1="{cy - 8}" x2="{cx + 12}" y2="{cy - 8}" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" opacity=".6"/>

          <!-- Far Lens (Foreshortened in 3/4 perspective) -->
          <rect x="{cx - 24}" y="{cy - 12}" width="16" height="14" rx="3.5" fill="#080c18" fill-opacity=".2" stroke="#0f172a" stroke-width="1.8"/>
          <rect x="{cx - 24}" y="{cy - 12}" width="16" height="14" rx="3.5" fill="none" stroke="#22d3ee" stroke-width="0.8" stroke-opacity=".8"/>
          <line x1="{cx - 21}" y1="{cy - 8}" x2="{cx - 15}" y2="{cy - 8}" stroke="#ffffff" stroke-width="1" stroke-linecap="round" opacity=".5"/>

          <!-- Bridge -->
          <path d="M{cx - 8} {cy - 6} Q{cx - 5} {cy - 8} {cx - 2} {cy - 6}" stroke="#0f172a" stroke-width="2" fill="none"/>
          <path d="M{cx - 8} {cy - 6} Q{cx - 5} {cy - 8} {cx - 2} {cy - 6}" stroke="#22d3ee" stroke-width="1" stroke-opacity=".8" fill="none"/>

          <!-- Temple arms to ears -->
          <path d="M{cx - 24} {cy - 7} L{cx - 29} {cy - 6}" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
          <path d="M{cx + 20} {cy - 7} L{cx + 25} {cy - 6}" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
        </g>
    ''' if glasses else ''

    mouth_markup = f'''
        <path d="M{cx - 2} {cy + 15} Q{cx + 6} {cy + 19} {cx + 14} {cy + 14}" stroke="#78350f" stroke-width="2.2" stroke-linecap="round" fill="none"/>
        <path d="M{cx + 1} {cy + 16} Q{cx + 6} {cy + 18} {cx + 11} {cy + 16}" stroke="#a16207" stroke-width="1.2" stroke-linecap="round" fill="none" opacity=".5"/>
    ''' if expression == "smile" else f'''
        <path d="M{cx - 2} {cy + 15} Q{cx + 5} {cy + 17} {cx + 12} {cy + 13}" stroke="#78350f" stroke-width="2.2" stroke-linecap="round" fill="none"/>
    '''

    return f'''
      <!-- SUBHAJIT KAR HEAD (3/4 ATHLETIC VIEW) -->
      <g id="subhajit_head" transform="rotate({angle_deg} {cx} {cy})">
        <!-- Neck -->
        <path fill="#cb7c4d" d="M{cx - 12} {cy + 16} C{cx - 14} {cy + 28} {cx - 16} {cy + 42} {cx - 18} {cy + 48} L{cx + 16} {cy + 48} C{cx + 14} {cy + 40} {cx + 12} {cy + 26} {cx + 10} {cy + 16} Z"/>
        <path fill="#e6a277" d="M{cx - 10} {cy + 16} C{cx - 12} {cy + 26} {cx - 13} {cy + 40} {cx - 14} {cy + 48} L{cx + 13} {cy + 48} C{cx + 12} {cy + 40} {cx + 10} {cy + 26} {cx + 8} {cy + 16} Z"/>
        <path d="M{cx - 4} {cy + 24} Q{cx - 8} {cy + 36} {cx - 10} {cy + 48}" stroke="#b45309" stroke-width="1.4" stroke-linecap="round" fill="none" opacity=".4"/>

        <!-- Far Ear (Left) -->
        <ellipse cx="{cx - 27}" cy="{cy + 2}" rx="4" ry="6" fill="#e6a277"/>
        <path d="M{cx - 28} {cy - 1} C{cx - 26} {cy + 2} {cx - 27} {cy + 4} {cx - 28} {cy + 5}" stroke="#cb7c4d" stroke-width="1.2" fill="none"/>

        <!-- Face Base (Organic 3/4 Masculine Profile) -->
        <path fill="#e6a277" d="M{cx - 25} {cy - 14} C{cx - 27} {cy + 6} {cx - 18} {cy + 24} {cx + 1} {cy + 27} C{cx + 12} {cy + 27} {cx + 22} {cy + 18} {cx + 25} {cy + 4} C{cx + 28} {cy - 8} {cx + 25} {cy - 24} {cx + 18} {cy - 34} C{cx + 6} {cy - 36} {cx - 15} {cy - 36} {cx - 25} {cy - 14} Z"/>
        
        <!-- Jaw & Cheek Shadow Structure -->
        <path fill="#cb7c4d" d="M{cx - 24} {cy} C{cx - 25} {cy + 14} {cx - 16} {cy + 24} {cx + 1} {cy + 27} C{cx - 6} {cy + 26} {cx - 18} {cy + 16} {cx - 21} {cy} Z" opacity=".4"/>
        <!-- Chin contour -->
        <path d="M{cx - 4} {cy + 22} Q{cx + 1} {cy + 24} {cx + 6} {cy + 22}" stroke="#b45309" stroke-width="1.8" stroke-linecap="round" fill="none" opacity=".4"/>

        <!-- Neat Trimmed Stubble / Beard Shadow -->
        <path fill="#0b0e1a" opacity=".12" d="M{cx - 21} {cy + 8} C{cx - 18} {cy + 21} {cx - 10} {cy + 26} {cx + 1} {cy + 26} C{cx + 10} {cy + 26} {cx + 18} {cy + 20} {cx + 20} {cy + 8} C{cx + 18} {cy + 17} {cx + 8} {cy + 23} {cx + 1} {cy + 24} C{cx - 8} {cy + 23} {cx - 18} {cy + 17} {cx - 21} {cy + 8} Z"/>

        <!-- Eyebrows (Focused, masculine) -->
        <path d="M{cx - 21} {cy - 16} Q{cx - 14} {cy - 21} {cx - 6} {cy - 16}" stroke="#0b0e1a" stroke-width="2.6" stroke-linecap="round" fill="none"/>
        <path d="M{cx + 2} {cy - 16} Q{cx + 10} {cy - 21} {cx + 19} {cy - 17}" stroke="#0b0e1a" stroke-width="2.6" stroke-linecap="round" fill="none"/>

        <!-- Eyes (Looking focused toward action) -->
        <!-- Far Eye -->
        <ellipse cx="{cx - 13}" cy="{cy - 6}" rx="4" ry="2.8" fill="#ffffff"/>
        <circle cx="{cx - 12}" cy="{cy - 5.5}" r="2" fill="#0b0e1a"/>
        <circle cx="{cx - 11}" cy="{cy - 6.5}" r="0.7" fill="#ffffff"/>

        <!-- Near Eye (Larger) -->
        <ellipse cx="{cx + 10}" cy="{cy - 6}" rx="4.8" ry="3.2" fill="#ffffff"/>
        <circle cx="{cx + 11.5}" cy="{cy - 5.5}" r="2.3" fill="#0b0e1a"/>
        <circle cx="{cx + 12.5}" cy="{cy - 6.5}" r="0.8" fill="#ffffff"/>

        <!-- Nose (3/4 perspective) -->
        <path d="M{cx + 1} {cy - 12} L{cx + 4} {cy + 4} L{cx - 1} {cy + 6}" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>

        <!-- Mouth -->
        {mouth_markup}

        <!-- Spectacles -->
        {glasses_markup}

        <!-- Canonical Male Short Fade Haircut (Subhajit Kar) -->
        <!-- Temple Fade & Taper (Clean line above ear) -->
        <path fill="#0b0e1a" d="M{cx - 26} {cy - 8} C{cx - 28} {cy - 20} {cx - 22} {cy - 34} {cx - 10} {cy - 40} L{cx - 16} {cy - 18} Z"/>
        <!-- Dense Textured Top & Crown Volume -->
        <path fill="#0b0e1a" d="M{cx - 26} {cy - 16} C{cx - 30} {cy - 38} {cx - 12} {cy - 48} {cx + 4} {cy - 48} C{cx + 20} {cy - 48} {cx + 34} {cy - 36} {cx + 26} {cy - 16} C{cx + 20} {cy - 28} {cx + 10} {cy - 36} {cx - 2} {cy - 34} C{cx - 14} {cy - 36} {cx - 22} {cy - 28} {cx - 26} {cy - 16} Z"/>
        <!-- Subtle Wave Highlights -->
        <path fill="#1e293b" d="M{cx - 16} {cy - 40} C{cx - 6} {cy - 46} {cx + 12} {cy - 46} {cx + 22} {cy - 36} C{cx + 14} {cy - 42} {cx + 2} {cy - 44} {cx - 10} {cy - 38} Z" opacity=".85"/>
        <path d="M{cx - 10} {cy - 40} Q{cx + 2} {cy - 44} {cx + 14} {cy - 38}" stroke="#334155" stroke-width="1.8" stroke-linecap="round" fill="none" opacity=".8"/>
        <!-- Hairline Edge -->
        <path fill="#0b0e1a" d="M{cx - 24} {cy - 22} C{cx - 16} {cy - 32} {cx - 4} {cy - 30} {cx + 2} {cy - 28} C{cx + 8} {cy - 30} {cx + 18} {cy - 32} {cx + 24} {cy - 22} C{cx + 17} {cy - 26} {cx + 8} {cy - 25} {cx + 2} {cy - 24} C{cx - 6} {cy - 25} {cx - 16} {cy - 26} {cx - 24} {cy - 22} Z"/>
      </g>
    '''

def generate_football_scene():
    """
    Scene 1: ⚽ Male Football Player (Subhajit Kar)
    Dynamic volley strike pose with organic human bezier curves,
    regulation 32-panel soccer ball, pitch turf, and energy trails.
    """
    head = get_subhajit_head(cx=205, cy=95, angle_deg=8, looking="down_right", expression="confident", glasses=True)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <!-- Soccer Ball Radial Shader -->
    <radialGradient id="fbBallShade" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </radialGradient>
    <!-- Pitch Turf Radial Glow -->
    <radialGradient id="fbTurfGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity=".45"/>
      <stop offset="60%" stop-color="#059669" stop-opacity=".15"/>
      <stop offset="100%" stop-color="#047857" stop-opacity="0"/>
    </radialGradient>
    <!-- Football Jersey Gradient -->
    <linearGradient id="fbJersey" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#151c2e"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <!-- Cyan Strike Trail -->
    <linearGradient id="fbSpeedTrail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity=".9"/>
      <stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- PITCH TURF & ATHLETIC SHADOW -->
  <g id="pitch_ground">
    <ellipse cx="230" cy="338" rx="145" ry="16" fill="url(#fbTurfGlow)"/>
    <!-- Ground Foot Shadow -->
    <ellipse cx="178" cy="336" rx="30" ry="6" fill="#022c22" opacity=".4"/>
    <!-- Ball Shadow -->
    <ellipse cx="365" cy="328" rx="26" ry="5" fill="#022c22" opacity=".25">
      <animate attributeName="rx" values="26; 22; 26" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".25; .18; .25" dur="2s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- BALL SPEED BURST TRAILS -->
  <g opacity=".85">
    <path d="M285 278 C310 274 335 264 365 252" stroke="url(#fbSpeedTrail)" stroke-width="4.5" stroke-linecap="round" fill="none">
      <animate attributeName="stroke-dasharray" values="10,60; 50,10; 10,60" dur="1.8s" repeatCount="indefinite"/>
    </path>
    <path d="M280 290 C310 286 340 276 375 266" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".6">
      <animate attributeName="stroke-dasharray" values="20,40; 60,10; 20,40" dur="1.8s" repeatCount="indefinite"/>
    </path>
    <path d="M290 302 C320 300 345 292 370 282" stroke="#34d399" stroke-width="1.8" stroke-linecap="round" fill="none" opacity=".5"/>
  </g>

  <!-- PLAYER CHARACTER: SUBHAJIT KAR -->
  <g id="football_player">
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -4; 0 0" dur="2s" repeatCount="indefinite" ease="ease-in-out"/>

    <!-- LEFT SUPPORT LEG (ORGANIC HUMAN BEZIER ANATOMY) -->
    <g id="support_leg">
      <!-- Thigh -->
      <path fill="#cb7c4d" d="M185 200 C180 216 174 238 172 258 C180 262 192 260 198 256 C202 236 206 215 208 200 Z"/>
      <path fill="#e6a277" d="M183 200 C178 218 174 240 174 257 C181 260 190 259 196 256 C200 238 204 218 206 200 Z"/>
      <!-- Knee & Calf -->
      <path fill="#cb7c4d" d="M172 258 C168 276 168 298 170 318 C176 321 184 321 188 318 C192 300 194 278 198 256 Z"/>
      <path fill="#e6a277" d="M174 257 C171 274 171 296 173 318 C177 320 184 320 186 318 C190 300 192 278 196 256 Z"/>
      <!-- White Football Sock with Cyan Band -->
      <path fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" d="M170 295 C169 305 170 316 171 324 L189 324 C190 316 190 305 189 295 Z"/>
      <line x1="170" y1="300" x2="189" y2="300" stroke="#22d3ee" stroke-width="2"/>
      <!-- Planted Football Boot / Cleat -->
      <path fill="#0f172a" d="M169 322 C165 325 158 329 152 332 C150 334 153 336 160 336 L194 336 C197 336 198 333 196 330 C193 325 188 322 184 322 Z"/>
      <path fill="#22d3ee" d="M164 332 L184 330 L186 333 L166 335 Z"/>
      <rect x="156" y="336" width="4" height="3" rx="1" fill="#22d3ee"/>
      <rect x="170" y="336" width="4" height="3" rx="1" fill="#cbd5e1"/>
      <rect x="188" y="336" width="4" height="3" rx="1" fill="#22d3ee"/>
    </g>

    <!-- RIGHT KICKING LEG (SWEPT IN DYNAMIC VOLLEY STRIKE) -->
    <g id="kicking_leg">
      <!-- Thigh extending diagonally backward to forward -->
      <path fill="#cb7c4d" d="M218 198 C232 208 258 226 278 240 C284 234 280 224 272 218 C252 202 232 194 222 194 Z"/>
      <path fill="#e6a277" d="M216 196 C230 206 256 224 276 238 C281 233 278 224 270 217 C250 201 230 193 220 193 Z"/>
      <!-- Calf sweeping explosively forward into the ball -->
      <path fill="#cb7c4d" d="M278 240 C294 246 314 258 330 272 C334 266 330 256 322 250 C306 238 290 230 278 240 Z"/>
      <path fill="#e6a277" d="M276 238 C292 244 312 256 328 270 C332 265 328 256 320 249 C304 237 288 229 276 238 Z"/>
      <!-- Sock -->
      <path fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" d="M312 258 L330 272 L338 266 L320 252 Z"/>
      <line x1="316" y1="260" x2="324" y2="254" stroke="#22d3ee" stroke-width="2"/>
      <!-- Striking Cleat (Volleying through the ball) -->
      <path fill="#0f172a" d="M328 268 C334 272 346 278 358 282 C362 284 364 282 360 278 L342 260 C338 256 332 256 328 260 Z"/>
      <path fill="#22d3ee" d="M336 270 L356 278 L354 281 L334 273 Z"/>
      <polygon points="344,282 347,287 350,283" fill="#22d3ee"/>
      <polygon points="356,284 359,288 362,285" fill="#cbd5e1"/>
    </g>

    <!-- ATHLETIC APPAREL -->
    <!-- Match Shorts -->
    <path fill="#151c2e" d="M186 182 C180 192 176 210 178 218 L208 215 L214 202 L224 213 L248 202 C246 193 238 183 228 181 Z"/>
    <path d="M178 217 L206 214" stroke="#22d3ee" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M224 212 L246 201" stroke="#22d3ee" stroke-width="2.2" stroke-linecap="round"/>

    <!-- Football Jersey (Navy & Electric Cyan #10) -->
    <path fill="url(#fbJersey)" d="M182 135 C174 148 170 168 182 188 C192 190 226 188 232 184 C239 166 238 146 234 135 C224 132 194 132 182 135 Z"/>
    <!-- Cyan Aerodynamic Side Panels -->
    <path fill="#22d3ee" d="M182 135 C178 150 176 170 182 188 C186 188 187 180 186 166 C185 150 188 138 190 135 Z" opacity=".9"/>
    <path fill="#22d3ee" d="M234 135 C238 150 238 170 232 184 C228 184 227 178 228 166 C229 150 227 138 225 135 Z" opacity=".9"/>
    <!-- Collar V-Neck -->
    <path d="M202 134 L208 144 L214 134" stroke="#22d3ee" stroke-width="2" fill="none"/>
    <!-- Subhajit #10 on Jersey -->
    <text x="208" y="164" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="15" fill="#ffffff" text-anchor="middle" letter-spacing="1">10</text>

    <!-- LEFT ARM (EXTENDED FOR BALANCE) -->
    <path fill="#cb7c4d" d="M182 140 C169 146 152 156 140 168 C139 174 145 178 151 174 C163 164 176 154 186 150 Z"/>
    <path fill="#e6a277" d="M180 138 C167 144 150 154 139 166 C138 172 143 176 149 172 C161 162 174 152 184 148 Z"/>
    <ellipse cx="136" cy="170" rx="5.5" ry="4.5" fill="#e6a277"/>

    <!-- RIGHT ARM (PULLED BACK IN SHOOTING RHYTHM) -->
    <path fill="#cb7c4d" d="M232 142 C246 146 262 154 274 166 C278 172 274 178 268 175 C256 165 244 156 232 152 Z"/>
    <path fill="#e6a277" d="M230 140 C244 144 260 152 272 164 C276 170 272 176 266 173 C254 163 242 154 230 150 Z"/>
    <ellipse cx="276" cy="170" rx="5.5" ry="4.5" fill="#e6a277"/>

    <!-- HEAD -->
    {head}
  </g>

  <!-- ⚽ REGULATION 32-PANEL SOCCER BALL (ANIMATED VOLLEY STRIKE) -->
  <g id="soccer_ball" transform="translate(365, 255)">
    <animateTransform attributeName="transform" type="translate" values="365 255; 372 248; 365 255" dur="2s" repeatCount="indefinite" ease="ease-in-out"/>
    
    <g>
      <animateTransform attributeName="transform" type="rotate" values="0; 360" dur="3s" repeatCount="indefinite"/>
      <!-- Sphere Base -->
      <circle cx="0" cy="0" r="28" fill="url(#fbBallShade)" stroke="#0f172a" stroke-width="1.2"/>
      
      <!-- Central Black Pentagon -->
      <polygon points="0,-10 9.5,-3 5.9,8 -5.9,8 -9.5,-3" fill="#0f172a"/>
      
      <!-- Seam lines radiating from central pentagon -->
      <line x1="0" y1="-10" x2="0" y2="-20" stroke="#0f172a" stroke-width="1.4"/>
      <line x1="9.5" y1="-3" x2="19" y2="-7" stroke="#0f172a" stroke-width="1.4"/>
      <line x1="5.9" y1="8" x2="14" y2="18" stroke="#0f172a" stroke-width="1.4"/>
      <line x1="-5.9" y1="8" x2="-14" y2="18" stroke="#0f172a" stroke-width="1.4"/>
      <line x1="-9.5" y1="-3" x2="-19" y2="-7" stroke="#0f172a" stroke-width="1.4"/>

      <!-- Peripheral Black Patches -->
      <polygon points="-7,-22 0,-20 7,-22 5,-28 -5,-28" fill="#0f172a"/>
      <polygon points="19,-7 25,-12 28,-4 22,2" fill="#0f172a"/>
      <polygon points="14,18 22,20 20,26 12,24" fill="#0f172a"/>
      <polygon points="-14,18 -22,20 -20,26 -12,24" fill="#0f172a"/>
      <polygon points="-19,-7 -25,-12 -28,-4 -22,2" fill="#0f172a"/>

      <!-- Specular Highlight -->
      <ellipse cx="-8" cy="-8" rx="7" ry="4" fill="#ffffff" opacity=".5" transform="rotate(-30 -8 -8)"/>
    </g>
  </g>

  <!-- TURF KICK-UP PARTICLES -->
  <g>
    <circle cx="348" cy="260" r="2.2" fill="#fde047">
      <animate attributeName="opacity" values="0;1;0" dur="0.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="338" cy="274" r="1.6" fill="#22d3ee">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </circle>
    <path d="M178 335 Q182 324 188 322" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    <path d="M174 336 Q170 326 166 324" stroke="#10b981" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>
</svg>'''

def generate_badminton_scene():
    """
    Scene 2: 🏸 Male Badminton Player (Subhajit Kar)
    Airborne jump-smash pose, angled athletic body, high-tension isometric racket,
    feathered shuttlecock with trajectory, and court energy lines.
    """
    head = get_subhajit_head(cx=210, cy=102, angle_deg=-6, looking="up_right", expression="confident", glasses=True)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <!-- Court Floor Glow -->
    <radialGradient id="bmFloorGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity=".35"/>
      <stop offset="60%" stop-color="#d97706" stop-opacity=".12"/>
      <stop offset="100%" stop-color="#b45309" stop-opacity="0"/>
    </radialGradient>
    <!-- Performance Jersey -->
    <linearGradient id="bmJersey" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <!-- Racket Frame Gradient -->
    <linearGradient id="bmRacketFrame" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#fbbf24"/>
    </linearGradient>
    <!-- Smash Speed Trail -->
    <linearGradient id="bmSpeedTrail" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity=".9"/>
      <stop offset="50%" stop-color="#f59e0b" stop-opacity=".5"/>
      <stop offset="100%" stop-color="#fbbf24" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- COURT FLOOR SHADOW -->
  <g id="court_ground">
    <ellipse cx="230" cy="338" rx="130" ry="14" fill="url(#bmFloorGlow)"/>
    <!-- Airborne dynamic suspended shadow (smaller & softer to indicate leap) -->
    <ellipse cx="220" cy="336" rx="46" ry="7" fill="#451a03" opacity=".25">
      <animate attributeName="rx" values="46; 40; 46" dur="2.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".25; .18; .25" dur="2.2s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- SMASH SPEED TRAIL ARC -->
  <g>
    <path d="M260 50 C320 60 360 110 380 160" stroke="url(#bmSpeedTrail)" stroke-width="4.5" stroke-linecap="round" fill="none">
      <animate attributeName="stroke-dasharray" values="20,100; 120,20; 20,100" dur="2.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".4; .9; .4" dur="2.2s" repeatCount="indefinite"/>
    </path>
    <path d="M275 65 C325 80 355 120 370 165" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" fill="none" opacity=".6"/>
  </g>

  <!-- AIRBORNE PLAYER: SUBHAJIT KAR -->
  <g id="badminton_player">
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -10; 0 0" dur="2.2s" repeatCount="indefinite" ease="ease-in-out"/>

    <!-- LEFT LEG (SCISSOR KICK BENT BACKWARD) -->
    <g id="left_leg">
      <!-- Thigh -->
      <path fill="#cb7c4d" d="M188 200 C174 214 158 232 148 252 C154 257 166 255 172 249 C184 232 196 215 202 200 Z"/>
      <path fill="#e6a277" d="M186 200 C172 214 156 232 146 251 C152 256 164 254 170 248 C182 232 194 215 200 200 Z"/>
      <!-- Lower Leg & Foot tucked backward -->
      <path fill="#cb7c4d" d="M148 252 C140 270 134 290 132 306 C138 308 146 306 150 302 C154 288 162 268 172 249 Z"/>
      <path fill="#e6a277" d="M146 251 C138 269 133 289 131 305 C136 307 144 305 148 301 C152 287 160 267 170 248 Z"/>
      <!-- Sock -->
      <path fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" d="M132 294 L148 291 L150 302 L132 306 Z"/>
      <!-- Court Shoe -->
      <path fill="#0f172a" d="M131 304 C126 310 118 318 112 322 C110 324 114 326 120 324 L142 312 C146 310 148 306 146 302 Z"/>
      <path fill="#fbbf24" d="M118 322 L140 310 L142 312 L120 324 Z"/>
    </g>

    <!-- RIGHT LEG (FORWARD LANDING PREPARATION) -->
    <g id="right_leg">
      <!-- Thigh -->
      <path fill="#cb7c4d" d="M222 200 C232 216 246 240 252 262 C260 262 268 256 266 248 C256 228 242 208 232 198 Z"/>
      <path fill="#e6a277" d="M220 199 C230 215 244 239 250 261 C258 261 266 255 264 247 C254 227 240 207 230 197 Z"/>
      <!-- Lower leg angled down -->
      <path fill="#cb7c4d" d="M252 262 C254 280 254 300 252 318 C258 319 266 318 270 316 C272 298 270 276 266 248 Z"/>
      <path fill="#e6a277" d="M250 261 C252 279 252 299 250 317 C256 318 264 317 268 315 C270 297 268 275 264 247 Z"/>
      <!-- Sock -->
      <path fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" d="M250 298 C250 306 250 316 251 321 L269 319 C269 314 269 304 268 298 Z"/>
      <line x1="250" y1="302" x2="268" y2="300" stroke="#fbbf24" stroke-width="1.8"/>
      <!-- Court Shoe -->
      <path fill="#0f172a" d="M249 320 C246 324 240 330 236 332 C234 334 238 336 244 335 L274 329 C277 328 278 324 276 321 C272 319 266 319 262 319 Z"/>
      <path fill="#fbbf24" d="M242 333 L270 327 L272 329 L244 335 Z"/>
    </g>

    <!-- ATHLETIC APPAREL -->
    <!-- Court Shorts -->
    <path fill="#151c2e" d="M190 186 C180 198 176 214 178 221 L206 216 L214 204 L224 214 L248 208 C244 198 238 188 228 184 Z"/>
    <path d="M178 220 L204 215" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M224 213 L246 207" stroke="#22d3ee" stroke-width="2.2" stroke-linecap="round"/>

    <!-- Badminton Court Jersey -->
    <path fill="url(#bmJersey)" d="M184 138 C176 151 172 170 184 190 C196 192 228 190 234 186 C240 168 240 150 236 138 C226 134 198 134 184 138 Z"/>
    <!-- Dynamic Diagonal Speed Stripes -->
    <path d="M180 162 L226 141" stroke="#fbbf24" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M186 174 L232 153" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>

    <!-- LEFT ARM (REACHING UP TO SIGHT SHUTTLECOCK) -->
    <path fill="#cb7c4d" d="M184 142 C168 129 150 113 136 95 C132 91 128 95 132 101 C146 119 164 137 180 152 Z"/>
    <path fill="#e6a277" d="M182 140 C166 127 148 111 134 93 C130 89 126 93 130 99 C144 117 162 135 178 150 Z"/>
    <ellipse cx="130" cy="91" rx="5" ry="6" fill="#e6a277" transform="rotate(-30 130 91)"/>

    <!-- RIGHT ARM (RAISED HIGH READY TO SMASH) -->
    <path fill="#cb7c4d" d="M234 140 C246 126 260 106 272 84 C278 80 284 84 280 92 C268 114 254 136 240 152 Z"/>
    <path fill="#e6a277" d="M232 138 C244 124 258 104 270 82 C276 78 282 82 278 90 C266 112 252 134 238 150 Z"/>
    <ellipse cx="274" cy="80" rx="6.5" ry="6" fill="#e6a277"/>

    <!-- HEAD -->
    {head}

    <!-- 🏸 HIGH-TENSION ISOMETRIC BADMINTON RACKET -->
    <g id="badminton_racket" transform="translate(274, 80)">
      <!-- Grip -->
      <line x1="0" y1="0" x2="22" y2="-28" stroke="#ffffff" stroke-width="5.5" stroke-linecap="round"/>
      <line x1="3" y1="-4" x2="6" y2="-8" stroke="#0284c7" stroke-width="1.8"/>
      <line x1="9" y1="-12" x2="12" y2="-16" stroke="#0284c7" stroke-width="1.8"/>
      <line x1="15" y1="-20" x2="18" y2="-24" stroke="#0284c7" stroke-width="1.8"/>
      <!-- Shaft -->
      <line x1="22" y1="-28" x2="48" y2="-62" stroke="url(#bmRacketFrame)" stroke-width="2.6" stroke-linecap="round"/>
      <circle cx="48" cy="-62" r="2.5" fill="#22d3ee"/>
      
      <!-- Head Frame -->
      <g transform="translate(68, -88) rotate(48)">
        <ellipse cx="0" cy="0" rx="20" ry="28" fill="none" stroke="url(#bmRacketFrame)" stroke-width="3"/>
        <ellipse cx="0" cy="0" rx="20" ry="28" fill="#22d3ee" fill-opacity=".06"/>
        
        <!-- Cross-String Grid -->
        <g stroke="#ffffff" stroke-width="0.7" opacity=".75">
          <line x1="-12" y1="-20" x2="-12" y2="20"/>
          <line x1="-6" y1="-26" x2="-6" y2="26"/>
          <line x1="0" y1="-28" x2="0" y2="28"/>
          <line x1="6" y1="-26" x2="6" y2="26"/>
          <line x1="12" y1="-20" x2="12" y2="20"/>
          <line x1="-18" y1="-14" x2="18" y2="-14"/>
          <line x1="-20" y1="-7" x2="20" y2="-7"/>
          <line x1="-20" y1="0" x2="20" y2="0"/>
          <line x1="-20" y1="7" x2="20" y2="7"/>
          <line x1="-18" y1="14" x2="18" y2="14"/>
        </g>
      </g>
    </g>
  </g>

  <!-- 🏸 OFFICIAL FEATHERED SHUTTLECOCK -->
  <g id="shuttlecock" transform="translate(385, 120) rotate(135)">
    <animateTransform attributeName="transform" type="translate" values="385 120; 392 114; 385 120" dur="2.2s" repeatCount="indefinite" ease="ease-in-out"/>
    
    <!-- Speed streaks -->
    <g opacity=".7" stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round">
      <line x1="-14" y1="-24" x2="-26" y2="-40"/>
      <line x1="0" y1="-26" x2="0" y2="-44"/>
      <line x1="14" y1="-24" x2="26" y2="-40"/>
    </g>

    <!-- Feather Skirt -->
    <polygon points="-16,-18 16,-18 10,2 -10,2" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
    <line x1="-14" y1="-12" x2="14" y2="-12" stroke="#94a3b8" stroke-width="1"/>
    <line x1="-12" y1="-6" x2="12" y2="-6" stroke="#94a3b8" stroke-width="1"/>
    <line x1="-14" y1="-18" x2="-8" y2="2" stroke="#e2e8f0" stroke-width="0.8"/>
    <line x1="-6" y1="-18" x2="-3" y2="2" stroke="#e2e8f0" stroke-width="0.8"/>
    <line x1="6" y1="-18" x2="3" y2="2" stroke="#e2e8f0" stroke-width="0.8"/>
    <line x1="14" y1="-18" x2="8" y2="2" stroke="#e2e8f0" stroke-width="0.8"/>

    <!-- Red Ribbon Collar Band -->
    <rect x="-10" y="2" width="20" height="3" fill="#ef4444"/>

    <!-- Cork Base Dome -->
    <path d="M-9 5 C-9 14 9 14 9 5 Z" fill="#fef08a" stroke="#ca8a04" stroke-width="0.8"/>
  </g>
</svg>'''

def generate_cooking_scene():
    """
    Scene 3: 👨‍🍳 Male Cooking / Chef (Subhajit Kar)
    Modern kitchen countertop, induction glow, chef apron with rolled-up sleeves,
    cast iron skillet with pan toss, airborne sautéed ingredients, rising aromatic steam curls.
    """
    head = get_subhajit_head(cx=210, cy=95, angle_deg=6, looking="down_right", expression="smile", glasses=True)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <!-- Countertop Gradient -->
    <linearGradient id="ckCounter" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="30%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <!-- Induction Heat Glow -->
    <radialGradient id="ckHeatGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity=".7"/>
      <stop offset="40%" stop-color="#f97316" stop-opacity=".4"/>
      <stop offset="80%" stop-color="#f59e0b" stop-opacity=".1"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0"/>
    </radialGradient>
    <!-- Cast Iron Pan Shader -->
    <radialGradient id="ckPanShade" cx="40%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="60%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#090d16"/>
    </radialGradient>
    <!-- Chef Apron -->
    <linearGradient id="ckApron" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <!-- Olive Oil Bottle -->
    <linearGradient id="ckOilGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>

  <!-- KITCHEN COUNTERTOP & INDUCTION COOKTOP -->
  <g id="kitchen_counter">
    <polygon points="40,285 460,285 480,360 20,360" fill="url(#ckCounter)"/>
    <line x1="40" y1="285" x2="460" y2="285" stroke="#334155" stroke-width="2.5"/>
    <line x1="40" y1="287" x2="460" y2="287" stroke="#22d3ee" stroke-width="0.8" stroke-opacity=".5"/>

    <!-- Glowing Induction Burner Ring -->
    <g transform="translate(345, 305)">
      <ellipse cx="0" cy="0" rx="60" ry="16" fill="url(#ckHeatGlow)"/>
      <ellipse cx="0" cy="0" rx="55" ry="14" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="8,6" opacity=".8">
        <animate attributeName="stroke-dashoffset" values="0; 28" dur="4s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="0" cy="0" rx="36" ry="9" fill="none" stroke="#f97316" stroke-width="1.8" stroke-dasharray="6,4" opacity=".85"/>
      <ellipse cx="0" cy="0" rx="16" ry="4" fill="#fbbf24" opacity=".6">
        <animate attributeName="opacity" values=".4; .8; .4" dur="1.8s" repeatCount="indefinite"/>
      </ellipse>
    </g>

    <!-- Olive Oil Bottle & Pepper Mill on Left Counter -->
    <g transform="translate(85, 245)">
      <rect x="0" y="14" width="18" height="28" rx="3" fill="url(#ckOilGrad)"/>
      <rect x="5" y="6" width="8" height="8" rx="1" fill="#cbd5e1" opacity=".8"/>
      <rect x="6" y="0" width="6" height="6" rx="1" fill="#f59e0b"/>
      <line x1="4" y1="20" x2="4" y2="38" stroke="#ffffff" stroke-width="1.2" stroke-linecap="round" opacity=".5"/>
      
      <path d="M26 18 L38 18 L36 42 L28 42 Z" fill="#334155"/>
      <circle cx="32" cy="14" r="4" fill="#64748b"/>
    </g>
  </g>

  <!-- MALE CHEF: SUBHAJIT KAR -->
  <g id="chef_character">
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -2.5; 0 0" dur="2s" repeatCount="indefinite" ease="ease-in-out"/>

    <!-- LOWER BODY / LEGS BEHIND COUNTER -->
    <path fill="#0f172a" d="M190 265 L190 325 L238 325 L238 265 Z"/>

    <!-- LIFESTYLE DARK SHIRT WITH ROLLED-UP SLEEVES -->
    <path fill="#1e293b" d="M176 136 C160 145 148 165 146 188 L162 194 C166 178 174 162 184 150 Z"/>
    <path fill="#1e293b" d="M250 136 C266 145 278 165 280 188 L264 194 C260 178 252 162 242 150 Z"/>

    <!-- FOREARMS WITH ROLLED SLEEVE CUFFS (ORGANIC BEZIER) -->
    <!-- Left Forearm holding Tasting Spatula -->
    <g id="left_arm">
      <rect x="152" y="188" width="14" height="6" rx="2" fill="#334155" transform="rotate(15 152 188)"/>
      <path fill="#cb7c4d" d="M160 194 C172 210 188 226 206 238 C211 234 210 226 204 220 C190 210 176 196 168 190 Z"/>
      <path fill="#e6a277" d="M158 192 C170 208 186 224 204 236 C209 232 208 225 202 219 C188 209 174 195 166 188 Z"/>
      <ellipse cx="208" cy="236" rx="6" ry="5.5" fill="#e6a277"/>
      <!-- Wooden Chef Spatula -->
      <line x1="204" y1="238" x2="266" y2="248" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
      <polygon points="264,244 278,246 276,254 262,251" fill="#b45309"/>
    </g>

    <!-- Right Forearm holding Skillet Handle -->
    <g id="right_arm">
      <rect x="264" y="188" width="14" height="6" rx="2" fill="#334155" transform="rotate(-15 264 188)"/>
      <path fill="#cb7c4d" d="M270 194 C280 210 292 226 306 240 C311 236 309 228 302 222 C290 210 280 198 272 190 Z"/>
      <path fill="#e6a277" d="M268 192 C278 208 290 224 304 238 C309 234 307 227 300 221 C288 209 278 197 270 188 Z"/>
      <ellipse cx="308" cy="238" rx="6.5" ry="6" fill="#e6a277"/>
    </g>

    <!-- CHEF APRON (TAILORED SLATE WITH CYAN ACCENTS) -->
    <path d="M198 135 C198 146 230 146 230 135" stroke="#22d3ee" stroke-width="2.6" fill="none"/>
    <path fill="url(#ckApron)" d="M192 142 L236 142 L250 185 L246 280 L182 280 L178 185 Z"/>
    <path d="M192 142 L236 142 L250 185 L246 280 L182 280 L178 185 Z" stroke="#334155" stroke-width="1.2" fill="none"/>
    <rect x="198" y="215" width="32" height="24" rx="3" fill="#151c2e" stroke="#22d3ee" stroke-width="1.2"/>
    <path d="M208 218 L208 205 Q212 200 216 205 L216 218" stroke="#f59e0b" stroke-width="1.6" fill="#fbbf24"/>

    <!-- HEAD -->
    {head}
  </g>

  <!-- 🍳 ACTIVE PAN TOSS: CAST IRON SKILLET & FLIPPED INGREDIENTS -->
  <g id="pan_and_toss">
    <animateTransform attributeName="transform" type="rotate" values="0 315 250; -5 315 250; 0 315 250" dur="1.8s" repeatCount="indefinite" ease="ease-in-out"/>

    <!-- Cast Iron Skillet -->
    <g transform="translate(315, 248)">
      <path d="M-8 -6 L-38 -14" stroke="#090d16" stroke-width="7" stroke-linecap="round"/>
      <path d="M-8 -6 L-38 -14" stroke="#475569" stroke-width="1.8" stroke-linecap="round" opacity=".6"/>
      <circle cx="-38" cy="-14" r="2.5" fill="#e2e8f0" opacity=".5"/>

      <ellipse cx="36" cy="4" rx="52" ry="18" fill="#090d16" stroke="#475569" stroke-width="1.5"/>
      <ellipse cx="36" cy="5" rx="46" ry="14" fill="url(#ckPanShade)"/>
      <ellipse cx="36" cy="6" rx="40" ry="10" fill="#451a03" opacity=".6"/>
    </g>

    <!-- AIRBORNE INGREDIENTS (ANIMATED TOSS) -->
    <g transform="translate(351, 225)">
      <animateTransform attributeName="transform" type="translate" values="351 225; 351 200; 351 225" dur="1.8s" repeatCount="indefinite" ease="ease-in-out"/>
      
      <path d="M-15 -4 Q-6 -14 6 -8" stroke="#ef4444" stroke-width="3.5" stroke-linecap="round" fill="none"/>
      <ellipse cx="14" cy="-12" rx="5" ry="3.5" fill="#f59e0b" transform="rotate(25 14 -12)"/>
      <ellipse cx="-4" cy="-18" rx="4" ry="2.5" fill="#fbbf24"/>
      <path fill="#10b981" d="M10 -2 C6 -8 10 -14 16 -12 C20 -8 16 -2 10 -2 Z"/>
      <circle cx="-18" cy="-14" r="2.2" fill="#10b981"/>
      <circle cx="24" cy="-6" r="2" fill="#ef4444"/>

      <!-- Sizzle Sparkles -->
      <circle cx="2" cy="-16" r="1.5" fill="#fde047">
        <animate attributeName="opacity" values="0;1;0" dur="0.9s" repeatCount="indefinite"/>
      </circle>
      <circle cx="18" cy="-22" r="1.2" fill="#fde047">
        <animate attributeName="opacity" values="1;0;1" dur="0.7s" repeatCount="indefinite"/>
      </circle>
    </g>
  </g>

  <!-- AROMATIC RISING STEAM CURLS -->
  <g stroke="#ffffff" fill="none" stroke-linecap="round" opacity=".65">
    <path d="M335 235 C320 195 340 165 330 125" stroke-width="2.4">
      <animate attributeName="stroke-dasharray" values="40,80; 80,40" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0; .75; 0" dur="2.4s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0 0; -6 -20" dur="2.4s" repeatCount="indefinite"/>
    </path>
    <path d="M357 238 C370 200 353 170 365 130" stroke-width="2.6">
      <animate attributeName="stroke-dasharray" values="40,80; 80,40" dur="2.1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0; .85; 0" dur="2.1s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0 0; 6 -22" dur="2.1s" repeatCount="indefinite"/>
    </path>
    <path d="M375 240 C387 210 375 180 383 145" stroke-width="2">
      <animate attributeName="stroke-dasharray" values="30,70; 70,30" dur="2.7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0; .6; 0" dur="2.7s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0 0; 4 -16" dur="2.7s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>'''

if __name__ == '__main__':
    qa_dir = Path(__file__).resolve().parent.parent / "qa"
    qa_dir.mkdir(exist_ok=True)

    scenes = [
        ("fitness-football.svg", generate_football_scene()),
        ("fitness-badminton.svg", generate_badminton_scene()),
        ("fitness-cooking.svg", generate_cooking_scene()),
    ]

    for fname, svg in scenes:
        try:
            ET.fromstring(svg)
            print(f"✅ {fname} is 100% valid XML")
            (qa_dir / fname).write_text(svg, encoding="utf-8")
        except Exception as e:
            print(f"❌ {fname} XML error: {e}")
            raise e

    print("🎉 All 3 pristine scenes successfully generated & validated!")
