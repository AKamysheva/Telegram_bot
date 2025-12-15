CREATE TABLE IF NOT EXISTS Videos 
(
  id UUID PRIMARY KEY,
  video_created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  views_count INT,
  likes_count INT,
  reports_count INT,
  comments_count INT,
  creator_id VARCHAR(100) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS Video_snapshots 
(
  id UUID PRIMARY KEY,
  video_id UUID NOT NULL,
  FOREIGN KEY (video_id) REFERENCES videos (id) ON DELETE CASCADE,
  views_count INT,
  likes_count INT,
  reports_count INT,
  comments_count INT,
  delta_views_count INT,
  delta_likes_count INT,
  delta_reports_count INT,
  delta_comments_count INT,
  created_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_video_snapshots_video_id ON video_snapshots (video_id);
