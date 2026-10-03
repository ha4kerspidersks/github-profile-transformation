#!/usr/bin/env python3
"""
scripts/generate_fitness_illustrations.py
Generates the three standalone and integrated male fitness illustrations for Subhajit Kar:
1. FOOTBALL (⚽ Male football / soccer player in dynamic kicking motion)
2. BADMINTON (🏸 Male badminton player in dynamic smash / lunge motion)
3. COOKING (👨‍🍳 Male culinary artist in kitchen tossing skillet with rising steam)
"""

def get_subhajit_male_head(cx=0, cy=0, looking="forward", glasses=True):
    """
    Returns Subhajit Kar's canonical male head:
    - Short dark hair fade with textured modern top
    - Warm skin tone (#e6a277)
    - Strong masculine jawline & confident expression
    - Optional signature cyan tech glasses
    """
    glasses_markup = f'''
        <!-- Signature Cyan Tech Glasses -->
        <g id="glasses">
          <rect x="{cx - 19}" y="{cy - 12}" width="18" height="13" rx="3.5" fill="#080c18" fill-opacity=".3" stroke="#22d3ee" stroke-width="1.6"/>
          <rect x="{cx + 3}" y="{cy - 12}" width="18" height="13" rx="3.5" fill="#080c18" fill-opacity=".3" stroke="#22d3ee" stroke-width="1.6"/>
          <path d="M{cx - 1} {cy - 6} L{cx + 3} {cy - 6}" stroke="#22d3ee" stroke-width="1.8"/>
          <path d="M{cx - 19} {cy - 6} L{cx - 25} {cy - 5}" stroke="#22d3ee" stroke-width="1.6"/>
        </g>
    ''' if glasses else ''

    mouth_markup = f'''
        <path d="M{cx - 6} {cy + 13} Q{cx + 2} {cy + 16} {cx + 9} {cy + 13}" stroke="#78350f" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    ''' if looking == "smile" else f'''
        <path d="M{cx - 5} {cy + 13} Q{cx + 1} {cy + 14} {cx + 7} {cy + 12}" stroke="#78350f" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    '''

    return f'''
      <!-- Neck -->
      <path fill="#d17a4a" d="M{cx - 8} {cy + 16} L{cx + 10} {cy + 16} L{cx + 14} {cy + 34} L{cx - 12} {cy + 34} Z"/>
      <path fill="#e6a277" d="M{cx - 6} {cy + 16} L{cx + 8} {cy + 16} L{cx + 12} {cy + 34} L{cx - 10} {cy + 34} Z"/>
      
      <!-- Head / Face Base -->
      <path fill="#e6a277" d="M{cx - 20} {cy - 12} C{cx - 22} {cy + 10} {cx - 14} {cy + 25} {cx + 1} {cy + 25} C{cx + 16} {cy + 25} {cx + 23} {cy + 10} {cx + 21} {cy - 12} C{cx + 20} {cy - 28} {cx - 19} {cy - 28} {cx - 20} {cy - 12} Z"/>
      <!-- Cheek Shadow / Jaw Structure -->
      <path fill="#d17a4a" d="M{cx - 18} {cy} C{cx - 19} {cy + 12} {cx - 12} {cy + 23} {cx + 1} {cy + 25} C{cx - 6} {cy + 24} {cx - 15} {cy + 15} {cx - 16} {cy} Z" opacity=".4"/>
      
      <!-- Ear -->
      <ellipse cx="{cx - 20}" cy="{cy}" rx="4.5" ry="6" fill="#e6a277"/>
      <path d="M{cx - 21} {cy - 3} Q{cx - 18} {cy} {cx - 20} {cy + 3}" stroke="#d17a4a" stroke-width="1.2" fill="none"/>
      
      <!-- Eyebrows -->
      <path d="M{cx - 16} {cy - 14} Q{cx - 8} {cy - 17} {cx - 2} {cy - 13}" stroke="#0b0e1a" stroke-width="2.2" stroke-linecap="round" fill="none"/>
      <path d="M{cx + 5} {cy - 13} Q{cx + 12} {cy - 17} {cx + 19} {cy - 14}" stroke="#0b0e1a" stroke-width="2.2" stroke-linecap="round" fill="none"/>
      
      <!-- Eyes -->
      <ellipse cx="{cx - 9}" cy="{cy - 6}" rx="3.5" ry="2.5" fill="#ffffff"/>
      <circle cx="{cx - 8}" cy="{cy - 6}" r="1.8" fill="#0b0e1a"/>
      <circle cx="{cx - 7.5}" cy="{cy - 6.5}" r="0.6" fill="#ffffff"/>

      <ellipse cx="{cx + 12}" cy="{cy - 6}" rx="3.5" ry="2.5" fill="#ffffff"/>
      <circle cx="{cx + 13}" cy="{cy - 6}" r="1.8" fill="#0b0e1a"/>
      <circle cx="{cx + 13.5}" cy="{cy - 6.5}" r="0.6" fill="#ffffff"/>
      
      <!-- Nose -->
      <path d="M{cx + 1} {cy - 9} L{cx + 3} {cy + 5} L{cx - 1} {cy + 7}" stroke="#d17a4a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      
      {mouth_markup}
      {glasses_markup}
      
      <!-- Canonical Male Short Fade Haircut (Subhajit Kar) -->
      <!-- Side Fade & Taper (Sharp above ear) -->
      <path fill="#0b0e1a" d="M{cx - 22} {cy - 6} C{cx - 24} {cy - 18} {cx - 18} {cy - 30} {cx - 8} {cy - 34} L{cx - 15} {cy - 15} Z"/>
      <!-- Top Volume & Textured Waves -->
      <path fill="#0b0e1a" d="M{cx - 22} {cy - 14} C{cx - 25} {cy - 34} {cx - 10} {cy - 44} {cx + 8} {cy - 44} C{cx + 24} {cy - 44} {cx + 26} {cy - 28} {cx + 22} {cy - 14} C{cx + 16} {cy - 26} {cx + 4} {cy - 32} {cx - 8} {cy - 30} C{cx - 16} {cy - 28} {cx - 20} {cy - 20} {cx - 22} {cy - 14} Z"/>
      <!-- Subtle Texture Highlights -->
      <path fill="#1a233a" d="M{cx - 14} {cy - 38} C{cx - 4} {cy - 44} {cx + 12} {cy - 43} {cx + 20} {cy - 32} C{cx + 14} {cy - 38} {cx + 2} {cy - 40} {cx - 10} {cy - 36} Z" opacity=".8"/>
      <path d="M{cx - 8} {cy - 36} Q{cx + 4} {cy - 40} {cx + 14} {cy - 34}" stroke="#25355a" stroke-width="1.8" stroke-linecap="round" fill="none" opacity=".7"/>
    '''

def generate_football_scene():
    """
    Scene 1: ⚽ Male Football Player (Subhajit Kar)
    Dynamic kicking / volley pose with spinning soccer ball and turf particles.
    """
    head = get_subhajit_male_head(cx=220, cy=115, looking="forward", glasses=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <radialGradient id="ballShade" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#e2e8f0"/>
      <stop offset="100%" stop-color="#94a3b8"/>
    </radialGradient>
    <linearGradient id="jerseyGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="turfGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0"/>
      <stop offset="30%" stop-color="#10b981" stop-opacity=".35"/>
      <stop offset="70%" stop-color="#10b981" stop-opacity=".35"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Pitch Ground Line & Shadow -->
  <line x1="60" y1="318" x2="440" y2="318" stroke="url(#turfGrad)" stroke-width="2.5" stroke-linecap="round"/>
  <ellipse cx="205" cy="320" rx="48" ry="10" fill="#000000" fill-opacity=".22">
    <animate attributeName="rx" values="48;40;48" dur="1.8s" repeatCount="indefinite"/>
  </ellipse>
  <ellipse cx="365" cy="318" rx="28" ry="6" fill="#000000" fill-opacity=".15">
    <animate attributeName="rx" values="28;34;28" dur="1.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".15;.08;.15" dur="1.8s" repeatCount="indefinite"/>
  </ellipse>

  <!-- Ground turf particles / kicking sparks -->
  <g fill="#10b981" opacity=".7">
    <circle cx="218" cy="316" r="2.2"><animate attributeName="cy" values="316;308;316" dur="0.9s" repeatCount="indefinite"/><animate attributeName="cx" values="218;230;218" dur="0.9s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="0.9s" repeatCount="indefinite"/></circle>
    <circle cx="225" cy="317" r="1.6"><animate attributeName="cy" values="317;305;317" dur="1.1s" repeatCount="indefinite"/><animate attributeName="cx" values="225;242;225" dur="1.1s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></circle>
    <circle cx="212" cy="318" r="1.8"><animate attributeName="cy" values="318;310;318" dur="0.75s" repeatCount="indefinite"/><animate attributeName="cx" values="212;202;212" dur="0.75s" repeatCount="indefinite"/></circle>
  </g>

  <!-- ATHLETE BODY (Subhajit Kar - Football) -->
  <g id="football_player">
    <!-- LEFT PLANT LEG (Anchored & Flexed) -->
    <!-- Thigh -->
    <path fill="#d17a4a" d="M192 205 L215 210 L195 265 L175 258 Z"/>
    <path fill="#e6a277" d="M195 206 L213 210 L196 262 L178 258 Z"/>
    <!-- Shin & Calf -->
    <path fill="#d17a4a" d="M176 258 L196 262 L202 312 L186 312 Z"/>
    <path fill="#e6a277" d="M178 258 L194 262 L200 310 L188 310 Z"/>
    <!-- Sock & Cleat -->
    <path fill="#141824" d="M185 285 L201 285 L203 315 L184 315 Z"/>
    <rect x="185" y="288" width="16" height="3" fill="#22d3ee"/>
    <!-- Left Shoe -->
    <path fill="#0f172a" d="M182 312 L205 312 L212 321 L180 321 Z"/>
    <path fill="#22d3ee" d="M188 316 L206 316" stroke="#22d3ee" stroke-width="1.8"/>
    <!-- Studs -->
    <circle cx="184" cy="322" r="1.5" fill="#38bdf8"/>
    <circle cx="208" cy="322" r="1.5" fill="#38bdf8"/>

    <!-- RIGHT KICKING LEG (Dynamic Forward Follow-Through) -->
    <g id="kicking_leg">
      <animateTransform attributeName="transform" type="rotate" values="0 230 205; 6 230 205; 0 230 205" dur="1.8s" repeatCount="indefinite"/>
      <!-- Thigh -->
      <path fill="#e6a277" d="M228 205 L252 202 L292 238 L272 248 Z"/>
      <path fill="#d17a4a" d="M228 205 L236 204 L276 247 L272 248 Z" opacity=".4"/>
      <!-- Shin (Extended toward ball) -->
      <path fill="#e6a277" d="M272 245 L292 236 L342 258 L330 270 Z"/>
      <!-- Right Sock -->
      <path fill="#141824" d="M308 248 L324 242 L340 262 L328 268 Z"/>
      <line x1="316" y1="244" x2="333" y2="263" stroke="#22d3ee" stroke-width="2.5"/>
      <!-- Right Cleat (Striking ball) -->
      <path fill="#0f172a" d="M328 264 L344 256 L362 268 L352 278 L332 274 Z"/>
      <path d="M336 268 L354 268" stroke="#22d3ee" stroke-width="2" stroke-linecap="round"/>
      <!-- Cleat Studs -->
      <circle cx="348" cy="278" r="1.5" fill="#38bdf8"/>
      <circle cx="358" cy="274" r="1.5" fill="#38bdf8"/>
    </g>

    <!-- ATHLETIC SHORTS (Navy Charcoal with Cyan Trim) -->
    <path fill="#1e293b" d="M186 195 L254 195 L258 232 L225 230 L220 216 L215 230 L180 228 Z"/>
    <!-- Cyan Stripe on Hem -->
    <path d="M180 227 L216 229" stroke="#22d3ee" stroke-width="2.5"/>
    <path d="M224 229 L258 231" stroke="#22d3ee" stroke-width="2.5"/>

    <!-- TORSO & HIGH-PERFORMANCE JERSEY -->
    <g id="torso">
      <!-- Jersey Body -->
      <path fill="url(#jerseyGrad)" d="M192 142 L250 138 L254 198 L188 198 Z"/>
      <!-- Cyan Athletic Side Panels -->
      <path fill="#22d3ee" d="M192 142 L200 142 L196 198 L188 198 Z" opacity=".85"/>
      <path fill="#22d3ee" d="M242 139 L250 138 L254 198 L246 198 Z" opacity=".85"/>
      <!-- V-Neck Collar Accent -->
      <path d="M214 140 L221 150 L228 140" stroke="#22d3ee" stroke-width="2.5" fill="none"/>
      <!-- Player Number 10 -->
      <text x="221" y="174" font-family="'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="16" fill="#ffffff" fill-opacity=".95" text-anchor="middle" letter-spacing="1">10</text>
    </g>

    <!-- LEFT ARM (Swung forward for balance) -->
    <g id="left_arm">
      <!-- Bicep -->
      <path fill="#e6a277" d="M194 144 L170 172 L180 180 L200 152 Z"/>
      <path fill="#22d3ee" d="M192 142 L202 150 L198 156 L188 146 Z"/> <!-- sleeve -->
      <!-- Forearm -->
      <path fill="#e6a277" d="M170 172 L146 186 L152 196 L178 180 Z"/>
      <!-- Hand Fist -->
      <ellipse cx="144" cy="192" rx="6" ry="5.5" fill="#e6a277"/>
    </g>

    <!-- RIGHT ARM (Cocked back for momentum) -->
    <g id="right_arm">
      <!-- Bicep -->
      <path fill="#e6a277" d="M248 140 L274 162 L266 172 L242 150 Z"/>
      <path fill="#22d3ee" d="M244 140 L254 148 L250 154 L240 144 Z"/> <!-- sleeve -->
      <!-- Forearm -->
      <path fill="#e6a277" d="M272 164 L294 184 L288 192 L266 172 Z"/>
      <!-- Hand -->
      <ellipse cx="296" cy="188" rx="5.5" ry="5" fill="#e6a277"/>
    </g>

    <!-- SUBHAJIT KAR HEAD & FACE -->
    {head}
  </g>

  <!-- SOCCER BALL (Spinning & Dynamic Motion) -->
  <g id="soccer_ball" transform="translate(365, 245)">
    <!-- Motion Speed Streaks -->
    <path d="M-60 2 L-20 2" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round" opacity=".5"/>
    <path d="M-50 -10 L-18 -6" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" opacity=".6"/>
    <path d="M-45 14 L-15 10" stroke="#34d399" stroke-width="2" stroke-linecap="round" opacity=".5"/>

    <!-- Spinning Ball Group -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2s" repeatCount="indefinite"/>
      <!-- Ball Spherical Base -->
      <circle cx="0" cy="0" r="22" fill="url(#ballShade)"/>
      <!-- Pentagons Pattern -->
      <!-- Center Pentagon -->
      <polygon points="0,-7 6,-2 4,6 -4,6 -6,-2" fill="#0f172a"/>
      <!-- Perimeter Patches -->
      <polygon points="0,-16 -4,-21 4,-21" fill="#0f172a"/>
      <polygon points="14,-5 20,-7 21,-2" fill="#0f172a"/>
      <polygon points="10,12 16,16 19,10" fill="#0f172a"/>
      <polygon points="-10,12 -16,16 -19,10" fill="#0f172a"/>
      <polygon points="-14,-5 -20,-7 -21,-2" fill="#0f172a"/>
      <!-- Seam Stitch Lines -->
      <line x1="0" y1="-7" x2="0" y2="-16" stroke="#64748b" stroke-width=".8"/>
      <line x1="6" y1="-2" x2="14" y2="-5" stroke="#64748b" stroke-width=".8"/>
      <line x1="4" y1="6" x2="10" y2="12" stroke="#64748b" stroke-width=".8"/>
      <line x1="-4" y1="6" x2="-10" y2="12" stroke="#64748b" stroke-width=".8"/>
      <line x1="-6" y1="-2" x2="-14" y2="-5" stroke="#64748b" stroke-width=".8"/>
      <!-- Subtle Specular Reflection -->
      <ellipse cx="-7" cy="-7" rx="6" ry="3" fill="#ffffff" opacity=".4" transform="rotate(-30 -7 -7)"/>
    </g>
  </g>
</svg>'''

def generate_badminton_scene():
    """
    Scene 2: 🏸 Male Badminton Player (Subhajit Kar)
    Dynamic jump-smash / airborne lunge pose with overhead racket, shuttlecock, and court lines.
    """
    head = get_subhajit_male_head(cx=210, cy=105, looking="forward", glasses=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <linearGradient id="badmintonJersey" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#141824"/>
      <stop offset="60%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="courtGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0"/>
      <stop offset="30%" stop-color="#fbbf24" stop-opacity=".4"/>
      <stop offset="70%" stop-color="#fbbf24" stop-opacity=".4"/>
      <stop offset="100%" stop-color="#fbbf24" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Court Floor Line & Perspective Marks -->
  <line x1="50" y1="322" x2="450" y2="322" stroke="url(#courtGrad)" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="120" y1="322" x2="160" y2="345" stroke="#fbbf24" stroke-opacity=".2" stroke-width="1.5"/>
  <line x1="380" y1="322" x2="340" y2="345" stroke="#fbbf24" stroke-opacity=".2" stroke-width="1.5"/>

  <!-- Dynamic Airborne Shadow -->
  <ellipse cx="215" cy="324" rx="46" ry="9" fill="#000000" fill-opacity=".2">
    <animate attributeName="rx" values="46;36;46" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".2;.1;.2" dur="2s" repeatCount="indefinite"/>
  </ellipse>

  <!-- BADMINTON SMASH SWING ARC TRAIL -->
  <path d="M260 30 Q330 65 310 160" stroke="#fbbf24" stroke-width="3.5" stroke-linecap="round" fill="none" opacity=".5">
    <animate attributeName="stroke-opacity" values=".2;.7;.2" dur="1.4s" repeatCount="indefinite"/>
    <animate attributeName="stroke-width" values="2;4.5;2" dur="1.4s" repeatCount="indefinite"/>
  </path>

  <!-- ATHLETE BODY (Airborne Smash Pose) -->
  <g id="badminton_player">
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -10; 0 0" dur="2s" repeatCount="indefinite"/>

    <!-- LEFT LEG (Back scissor kick leg) -->
    <g id="left_leg">
      <path fill="#e6a277" d="M188 198 L160 248 L174 256 L202 206 Z"/>
      <!-- Lower leg angled back -->
      <path fill="#e6a277" d="M162 250 L132 290 L144 298 L174 256 Z"/>
      <!-- Sneaker -->
      <path fill="#ffffff" d="M130 290 L118 306 L136 312 L146 296 Z"/>
      <path fill="#fbbf24" d="M120 306 L136 312 L132 316 L116 308 Z"/>
    </g>

    <!-- RIGHT LEG (Front landing lunge leg) -->
    <g id="right_leg">
      <path fill="#e6a277" d="M216 198 L244 246 L230 256 L204 206 Z"/>
      <!-- Lower leg extended downward -->
      <path fill="#e6a277" d="M242 248 L240 304 L254 304 L254 254 Z"/>
      <!-- Sneaker -->
      <path fill="#ffffff" d="M236 302 L230 316 L258 318 L256 302 Z"/>
      <path fill="#fbbf24" d="M230 315 L258 317 L256 320 L228 318 Z"/>
    </g>

    <!-- BADMINTON SHORTS -->
    <path fill="#1e293b" d="M182 188 L232 188 L246 226 L220 226 L210 210 L198 226 L174 226 Z"/>
    <!-- Gold / Amber Piping -->
    <path d="M174 224 L200 225" stroke="#fbbf24" stroke-width="2.5"/>
    <path d="M218 225 L246 225" stroke="#fbbf24" stroke-width="2.5"/>

    <!-- TORSO & ATHLETIC PERFORMANCE JERSEY -->
    <g id="jersey">
      <path fill="url(#badmintonJersey)" d="M186 132 L236 128 L232 192 L182 192 Z"/>
      <!-- Dynamic Diagonal Slashes (#fbbf24 & #22d3ee) -->
      <path d="M186 138 L234 176" stroke="#fbbf24" stroke-width="4" stroke-linecap="round"/>
      <path d="M184 150 L226 186" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/>
      <!-- Neckline -->
      <path d="M204 130 Q212 138 220 130" stroke="#fbbf24" stroke-width="2.2" fill="none"/>
    </g>

    <!-- LEFT ARM (Raised forward for sighting & aerial balance) -->
    <g id="left_sighting_arm">
      <path fill="#e6a277" d="M188 134 L154 116 L160 106 L194 126 Z"/>
      <!-- Forearm pointing toward shuttlecock -->
      <path fill="#e6a277" d="M156 114 L128 92 L136 84 L162 108 Z"/>
      <!-- Sighting Hand -->
      <path fill="#e6a277" d="M128 92 L118 78 L126 74 L134 86 Z"/>
    </g>

    <!-- RIGHT ARM (Cocked Overhead for Sledgehammer Smash) -->
    <g id="smash_arm">
      <!-- Upper Arm Reaching High Overhead -->
      <path fill="#e6a277" d="M234 130 L268 88 L280 96 L244 140 Z"/>
      <!-- Forearm Angled Forward -->
      <path fill="#e6a277" d="M268 90 L292 48 L304 54 L278 98 Z"/>
      <!-- Gold Wristband -->
      <rect x="290" y="48" width="14" height="6" rx="2" fill="#fbbf24" transform="rotate(-35 290 48)"/>
      <!-- Dominant Hand Gripping Racket Handle -->
      <ellipse cx="298" cy="46" rx="6" ry="7" fill="#e6a277" transform="rotate(-20 298 46)"/>
      
      <!-- BADMINTON RACKET -->
      <g id="racket">
        <!-- Handle & Grip Tape -->
        <line x1="288" y1="58" x2="315" y2="28" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
        <line x1="288" y1="58" x2="315" y2="28" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2 3"/>
        <!-- Carbon Fiber Shaft -->
        <line x1="315" y1="28" x2="352" y2="-12" stroke="#22d3ee" stroke-width="2.5" stroke-linecap="round"/>
        <!-- T-Joint -->
        <circle cx="352" cy="-12" r="2.8" fill="#fbbf24"/>
        <!-- Isometric Oval Racket Head Frame -->
        <ellipse cx="378" cy="-38" rx="34" ry="24" fill="none" stroke="#22d3ee" stroke-width="3" transform="rotate(-45 378 -38)"/>
        <!-- Fine String Mesh Grid -->
        <g stroke="#ffffff" stroke-opacity=".55" stroke-width=".8" transform="rotate(-45 378 -38)">
          <line x1="354" y1="-38" x2="402" y2="-38"/>
          <line x1="358" y1="-46" x2="398" y2="-46"/>
          <line x1="358" y1="-30" x2="398" y2="-30"/>
          <line x1="366" y1="-54" x2="390" y2="-54"/>
          <line x1="366" y1="-22" x2="390" y2="-22"/>
          <line x1="378" y1="-60" x2="378" y2="-16"/>
          <line x1="370" y1="-58" x2="370" y2="-18"/>
          <line x1="386" y1="-58" x2="386" y2="-18"/>
          <line x1="362" y1="-52" x2="362" y2="-24"/>
          <line x1="394" y1="-52" x2="394" y2="-24"/>
        </g>
      </g>
    </g>

    <!-- SUBHAJIT KAR HEAD & FACE -->
    {head}
  </g>

  <!-- SHUTTLECOCK (BIRDIE) IN HIGH-SPEED DESCENT -->
  <g id="shuttlecock" transform="translate(395, 60)">
    <!-- Speed Lines Behind Birdie -->
    <path d="M30 -24 L10 -8" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity=".6"/>
    <path d="M38 -12 L14 2" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round" opacity=".7"/>
    <path d="M26 4 L8 14" stroke="#22d3ee" stroke-width="1.8" stroke-linecap="round" opacity=".6"/>

    <g transform="rotate(130)">
      <!-- 16 Goose Feathers Cone -->
      <polygon points="0,0 -16,-28 16,-28" fill="#ffffff" fill-opacity=".92"/>
      <path d="M-14 -28 L0 0 L14 -28" stroke="#e2e8f0" stroke-width="1"/>
      <line x1="-12" y1="-20" x2="12" y2="-20" stroke="#cbd5e1" stroke-width="1.2"/>
      <line x1="-8" y1="-12" x2="8" y2="-12" stroke="#cbd5e1" stroke-width="1.2"/>
      <!-- Cork Rounded Base -->
      <ellipse cx="0" cy="0" rx="5.5" ry="5.5" fill="#f8fafc"/>
      <path d="M-5.5 0 A5.5 5.5 0 0 0 5.5 0 Z" fill="#e2e8f0"/>
      <!-- Red / Dark Ribbon Band on Cork -->
      <rect x="-5" y="-3" width="10" height="2" fill="#ef4444"/>
    </g>
  </g>
</svg>'''

def generate_cooking_scene():
    """
    Scene 3: 👨‍🍳 Male Cooking Scene (Subhajit Kar)
    Modern kitchen with induction cooktop, cast iron skillet toss, sizzling fresh ingredients & aromatic rising steam.
    """
    head = get_subhajit_male_head(cx=190, cy=105, looking="smile", glasses=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360" width="100%" height="100%">
  <defs>
    <linearGradient id="counterGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="25%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="apronGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <radialGradient id="flameGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f97316" stop-opacity=".9"/>
      <stop offset="40%" stop-color="#ef4444" stop-opacity=".5"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- KITCHEN COUNTERTOP & INDUCTION STOVE -->
  <g id="kitchen_counter">
    <!-- Counter Surface -->
    <polygon points="40,295 460,295 480,345 20,345" fill="url(#counterGrad)"/>
    <line x1="20" y1="295" x2="480" y2="295" stroke="#475569" stroke-width="2"/>
    <rect x="20" y="344" width="460" height="16" fill="#0f172a"/>
    
    <!-- Induction Hob Ring Glow -->
    <ellipse cx="320" cy="305" rx="55" ry="14" fill="none" stroke="#22d3ee" stroke-width="1.8" stroke-dasharray="8 6" opacity=".7"/>
    <ellipse cx="320" cy="305" rx="35" ry="9" fill="url(#flameGlow)" opacity=".6">
      <animate attributeName="opacity" values=".4;.85;.4" dur="1.2s" repeatCount="indefinite"/>
    </ellipse>

    <!-- Olive Oil Bottle on Counter -->
    <rect x="85" y="255" width="14" height="40" rx="3" fill="#10b981" fill-opacity=".4" stroke="#10b981" stroke-width="1.2"/>
    <rect x="89" y="247" width="6" height="8" fill="#f59e0b"/>
    <line x1="88" y1="270" x2="96" y2="270" stroke="#ffffff" stroke-opacity=".5"/>

    <!-- Spice Grinder -->
    <rect x="110" y="265" width="12" height="30" rx="2" fill="#475569" stroke="#64748b" stroke-width="1"/>
    <circle cx="116" cy="262" r="3" fill="#94a3b8"/>
  </g>

  <!-- CHEF / CULINARY ARTIST BODY (Subhajit Kar) -->
  <g id="chef_subhajit">
    <!-- LOWER BODY / PANTS -->
    <path fill="#0f172a" d="M165 245 L225 245 L230 335 L160 335 Z"/>

    <!-- TORSO & DARK LIFESTYLE SHIRT -->
    <path fill="#151c2e" d="M155 135 L235 135 L230 250 L160 250 Z"/>

    <!-- MODERN SLATE APRON WITH CYAN ACCENTS -->
    <g id="apron">
      <!-- Neck Strap -->
      <path d="M180 135 L175 145 L215 145 L210 135" stroke="#22d3ee" stroke-width="2.5" fill="none"/>
      <!-- Apron Bib & Skirt -->
      <path fill="url(#apronGrad)" stroke="#334155" stroke-width="1" d="M174 145 L216 145 L228 200 L228 290 L162 290 L162 200 Z"/>
      <!-- Apron Center Pocket -->
      <rect x="178" y="210" width="34" height="26" rx="4" fill="#1e293b" stroke="#22d3ee" stroke-width="1.2" stroke-opacity=".6"/>
      <!-- Wooden Tasting Spoon in Pocket -->
      <line x1="186" y1="210" x2="182" y2="192" stroke="#d97706" stroke-width="2.8" stroke-linecap="round"/>
      <ellipse cx="181" cy="189" rx="3.5" ry="5" fill="#d97706"/>
      <!-- Waist Ties -->
      <path d="M162 202 Q150 206 145 220" stroke="#22d3ee" stroke-width="2" fill="none"/>
      <path d="M228 202 Q240 206 245 220" stroke="#22d3ee" stroke-width="2" fill="none"/>
    </g>

    <!-- LEFT ARM & WOODEN SPATULA -->
    <g id="left_cooking_arm">
      <!-- Upper Arm with Rolled Sleeve -->
      <path fill="#e6a277" d="M156 138 L130 178 L142 186 L168 146 Z"/>
      <rect x="144" y="146" width="18" height="8" rx="2" fill="#22d3ee" transform="rotate(35 144 146)"/>
      <!-- Forearm -->
      <path fill="#e6a277" d="M132 180 L146 226 L158 222 L144 176 Z"/>
      <!-- Hand Gripping Spatula -->
      <ellipse cx="150" cy="230" rx="6" ry="5" fill="#e6a277"/>
      <!-- Wooden Spatula -->
      <line x1="150" y1="230" x2="240" y2="245" stroke="#d97706" stroke-width="3" stroke-linecap="round"/>
      <polygon points="240,241 258,244 256,252 238,249" fill="#d97706"/>
    </g>

    <!-- RIGHT ARM & CAST IRON SKILLET (Active Pan Toss) -->
    <g id="right_cooking_arm">
      <!-- Upper Arm with Rolled Sleeve -->
      <path fill="#e6a277" d="M232 138 L258 178 L246 186 L220 146 Z"/>
      <rect x="228" y="146" width="18" height="8" rx="2" fill="#22d3ee" transform="rotate(-35 228 146)"/>
      <!-- Forearm Extended to Pan Handle -->
      <path fill="#e6a277" d="M256 180 L286 215 L276 224 L246 188 Z"/>
      <!-- Hand Gripping Handle -->
      <ellipse cx="288" cy="216" rx="6.5" ry="6" fill="#e6a277"/>

      <!-- CAST IRON SKILLET & TOSS MOTION -->
      <g id="skillet_group" transform="translate(0, 0)">
        <animateTransform attributeName="transform" type="rotate" values="0 288 216; -4 288 216; 0 288 216" dur="1.6s" repeatCount="indefinite"/>
        <!-- Pan Handle -->
        <path d="M288 216 L310 236" stroke="#0f172a" stroke-width="6.5" stroke-linecap="round"/>
        <!-- Cast Iron Skillet Body -->
        <ellipse cx="345" cy="254" rx="42" ry="16" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
        <ellipse cx="345" cy="252" rx="38" ry="13" fill="#0f172a"/>
        <!-- Hot Oil / Sauce Glow -->
        <ellipse cx="345" cy="253" rx="30" ry="9" fill="#f59e0b" fill-opacity=".35"/>
      </g>
    </g>

    <!-- SUBHAJIT KAR HEAD & FACE -->
    {head}
  </g>

  <!-- AIRBORNE SIZZLING FOOD PARTICLES (Tossed from pan) -->
  <g id="tossed_food">
    <animateTransform attributeName="transform" type="translate" values="0 0; 0 -22; 0 0" dur="1.6s" repeatCount="indefinite"/>
    <!-- Red Bell Pepper Slice -->
    <path d="M336 226 Q342 220 348 224" stroke="#ef4444" stroke-width="3" stroke-linecap="round" fill="none"/>
    <!-- Golden Sautéed Carrot / Corn -->
    <ellipse cx="355" cy="222" rx="4" ry="2.5" fill="#f59e0b" transform="rotate(25 355 222)"/>
    <ellipse cx="330" cy="232" rx="3.5" ry="2" fill="#fbbf24"/>
    <!-- Fresh Green Herb / Basil Leaf -->
    <path fill="#10b981" d="M344 214 C340 210 344 204 350 206 C354 210 350 216 344 214 Z"/>
    <circle cx="362" cy="230" r="2.2" fill="#10b981"/>
    <!-- Sizzle Sparkles -->
    <circle cx="332" cy="216" r="1.5" fill="#fde047"><animate attributeName="opacity" values="0;1;0" dur="0.8s" repeatCount="indefinite"/></circle>
    <circle cx="358" cy="210" r="1.2" fill="#fde047"><animate attributeName="opacity" values="1;0;1" dur="0.6s" repeatCount="indefinite"/></circle>
  </g>

  <!-- AROMATIC RISING STEAM CURLS -->
  <g stroke="#ffffff" fill="none" stroke-linecap="round" opacity=".65">
    <!-- Steam Curl 1 -->
    <path d="M335 235 Q325 200 338 175 T332 135" stroke-width="2.2">
      <animate attributeName="stroke-dasharray" values="60;120" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;.7;0" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="transform" type="translate" values="0 0; -4 -16" dur="2.4s" repeatCount="indefinite"/>
    </path>
    <!-- Steam Curl 2 -->
    <path d="M352 238 Q365 205 354 180 T362 140" stroke-width="2.5">
      <animate attributeName="stroke-dasharray" values="60;120" dur="2.1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;.8;0" dur="2.1s" repeatCount="indefinite"/>
      <animate attributeName="transform" type="translate" values="0 0; 4 -18" dur="2.1s" repeatCount="indefinite"/>
    </path>
    <!-- Steam Curl 3 -->
    <path d="M365 240 Q378 215 370 190 T376 155" stroke-width="1.8">
      <animate attributeName="stroke-dasharray" values="40;80" dur="2.7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;.6;0" dur="2.7s" repeatCount="indefinite"/>
      <animate attributeName="transform" type="translate" values="0 0; 2 -14" dur="2.7s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>'''

if __name__ == '__main__':
    from pathlib import Path
    import xml.etree.ElementTree as ET

    out_dir = Path(__file__).resolve().parent.parent / "qa"
    out_dir.mkdir(exist_ok=True)

    scenes = [
        ("fitness-football.svg", generate_football_scene()),
        ("fitness-badminton.svg", generate_badminton_scene()),
        ("fitness-cooking.svg", generate_cooking_scene()),
    ]

    for filename, svg in scenes:
        try:
            ET.fromstring(svg)
            print(f"✅ {filename} is 100% valid XML")
            (out_dir / filename).write_text(svg, encoding="utf-8")
        except Exception as e:
            print(f"❌ {filename} XML error: {e}")
            raise e

    print("🎉 All 3 scenes generated and validated!")
